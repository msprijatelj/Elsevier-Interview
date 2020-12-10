import re
import json
import pandas as pd
from dateutil.parser import parse
from dateutil.relativedelta import relativedelta
from datetime import date
import flask

def birthDateToAge(dateStr):
    birthDate = parse(dateStr)
    realAge = relativedelta(date.today(), birthDate.date()).years
    outAge = str(realAge) if realAge < 90 else "90+"
    return outAge

def dateToYear(dateStr):
    fullDate = parse(dateStr)
    outYear = str(fullDate.year)
    return outYear

def stripZip(zipCode):
    zipCodeDf = pd.read_csv("populate_by_zcta_2010.csv")
    zipHead = zipCode[0:3]
    zipSubset = zipCodeDf.loc[zipCodeDf["Zip Code ZCTA"].startswith(zipHead)]
    totalPop = zipSubset["2010 Census Population"].astype(int).sum()
    outZipCode = f"{zipHead}00" if totalPop >= 20000 else "00000"
    return outZipCode

def redactEmail(msg):
    return msg

def redactSsn(msg):
    return msg

def redactPhone(msg):
    return msg

def redactDate(msg):
    return msg

def redactMessage(msg):
    msg = redactEmail(msg)
    msg = redactSsn(msg)
    msg = redactPhone(msg)
    msg = redactDate(msg)
    return msg

def handler(event):
    inputJson = json.loads(event)

    age = birthDateToAge(inputJson["birthDate"])
    zipCode = stripZip(inputJson["zipCode"])
    admissionYear = dateToYear(inputJson["admissionDate"])
    dischargeYear = dateToYear(inputJson["dischargeDate"])
    notes = redactMessage(inputJson["notes"])

    outputJson = {
        "age": age,
        "zipCode": zipCode,
        "admissionYear": admissionYear,
        "dischargeYear": dischargeYear,
        "notes": notes
    }

    return outputJson


if __name__ == "__main__":
    pass