import re
import json
import pandas as pd
from dateutil.parser import parse
from dateutil.relativedelta import relativedelta
from datetime import date
from flask import Flask
from flask_restful import Api, Resource, reqparse
import random

app = Flask(__name__)
api = Api(app)

def birthDateToAge(dateStr):
    try:
        birthDate = parse(dateStr)
        realAge = relativedelta(date.today(), birthDate.date()).years
        outAge = str(realAge) if realAge < 90 else "90+"
    except:
        outAge = "ERROR"
    return outAge

def dateToYear(dateStr):
    try:
        fullDate = parse(dateStr)
        outYear = str(fullDate.year)
    except:
        outYear = "ERROR"
    return outYear

def stripZip(zipCode):
    try:
        zipCodeDf = pd.read_csv("population_by_zcta_2010.csv")
        zipHead = int(zipCode[0:3])
        zipSeries = zipCodeDf["Zip Code ZCTA"].astype(int)
        zipSubset = zipCodeDf.loc[zipSeries.floordiv(100).eq(zipHead)]
        totalPop = zipSubset["2010 Census Population"].astype(int).sum()
        outZipCode = f"{zipHead}00" if totalPop >= 20000 else "00000"
    except FileNotFoundError as e:
        raise e
    except:
        outZipCode = "ERROR"
    return outZipCode

def redactEmail(msg):
    emailPattern = re.compile(r"(\S+)@(\S+)\.([a-zA-Z0-9]+)")
    emailRedact = "XXXXX@XXXXX.XXX"
    msg = emailPattern.sub(emailRedact, msg)
    return msg

def redactSsn(msg):
    ssnPattern = re.compile(
        r"([0-9]{3})[-]?([0-9]{2})[-]?([0-9]{4})")
    ssnRedact = "XXX-XX-XXXX"
    msg = ssnPattern.sub(ssnRedact, msg)
    return msg

def redactPhone(msg):
    phonePattern = re.compile(
        r"[(]?([0-9]{3})[)]?[ -]?([0-9A-Z]{3})[ -]?([0-9]{4})")
    phoneRedact = "(XXX) XXX-XXXX"
    msg = phonePattern.sub(phoneRedact, msg)
    return msg

def redactDate(msg):
    return msg

def redactMessage(msg):
    msg = redactEmail(msg)
    msg = redactPhone(msg)
    msg = redactSsn(msg)
    msg = redactDate(msg)
    return msg

parser = reqparse.RequestParser()
parser.add_argument('birthDate', type=str)
parser.add_argument('zipCode', type=str)
parser.add_argument('admissionDate', type=str)
parser.add_argument('dischargeDate', type=str)
parser.add_argument('notes', type=str)
class SafeHarbor(Resource):
    def post(self):
        args = parser.parse_args()

        age = birthDateToAge(args["birthDate"])
        zipCode = stripZip(args["zipCode"])
        admissionYear = dateToYear(args["admissionDate"])
        dischargeYear = dateToYear(args["dischargeDate"])
        notes = redactMessage(args["notes"])

        response = {
            "age": age,
            "zipCode": zipCode,
            "admissionYear": admissionYear,
            "dischargeYear": dischargeYear,
            "notes": notes
        }
        return response, 201

api.add_resource(SafeHarbor, "/")

if __name__ == "__main__":
    app.run(debug=True)