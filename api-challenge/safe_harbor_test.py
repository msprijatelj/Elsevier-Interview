import unittest
import re
from safe_harbor import birthDateToAge, dateToYear, stripZip, redactPhone,\
        redactEmail, redactSsn, redactMessage

class TestSafeHarbor(unittest.TestCase):
    PHONE_REDACT = "(XXX) XXX-XXXX"
    EMAIL_REDACT = "XXXXX@XXXXX.XXX"
    SSN_REDACT = "XXX-XX-XXXX"

    def testBirthDateToAge(self):
        birthDateSample = "2000-01-01"
        ageSample = birthDateToAge(birthDateSample)
        self.assertEqual(ageSample, "20")

        birthDateSample = "20000101"
        ageSample = birthDateToAge(birthDateSample)
        self.assertEqual(ageSample, "20")

        birthDateSample = "01/01/00"
        ageSample = birthDateToAge(birthDateSample)
        self.assertEqual(ageSample, "20")

        birthDateOver89 = "1930-01-01"
        ageOver89 = birthDateToAge(birthDateOver89)
        self.assertEqual(ageOver89, "90+")


    def testDateToYear(self):
        dateSample = "2019-03-12"
        yearSample = dateToYear(dateSample)
        self.assertEqual(yearSample, "2019")

        dateSample = "20190312"
        yearSample = dateToYear(dateSample)
        self.assertEqual(yearSample, "2019")

        dateSample = "03/12/19"
        yearSample = dateToYear(dateSample)
        self.assertEqual(yearSample, "2019")

    def testStripZip(self):
        zipCodeSample = "10013"
        strippedZipSample = stripZip(zipCodeSample)
        self.assertEqual(strippedZipSample, "10000")

        longZipCodeSample = "10013-4625"
        strippedLongZipSample = stripZip(longZipCodeSample)
        self.assertEqual(strippedLongZipSample, "10000")

        shortZipCodeSample = "100"
        strippedShortZipSample = stripZip(shortZipCodeSample)
        self.assertEqual(strippedShortZipSample, "10000")

        zeroZipCodeSample = "01023"
        strippedZeroZipSample = stripZip(zeroZipCodeSample)
        self.assertEqual(strippedZeroZipSample, "01000")

        zipCodeLowPop = "10271"
        strippedZipLowPop = stripZip(zipCodeLowPop)
        self.assertEqual(strippedZipLowPop, "00000")

    def testRedactPhone(self):

        testMsg = "1234567890 is a phone number"
        redactTestMsg = redactPhone(testMsg)
        self.assertEqual(redactTestMsg, f"{self.PHONE_REDACT} is a phone number")

        testMsg = "1234567890, 098-123-7654, & 123"
        redactTestMsg = redactPhone(testMsg)
        self.assertEqual(
            redactTestMsg, 
            f"{self.PHONE_REDACT}, {self.PHONE_REDACT}, & 123"
        )
    
    def testRedactEmail(self):

        testMsg = "Is abc.efg@hij.com? an email address?"
        redactTestMsg = redactEmail(testMsg)
        self.assertEqual(
            redactTestMsg, 
            f"Is {self.EMAIL_REDACT}? an email address?"
        )

    def testRedactSsn(self):

        testMsg = "Is 123-45-6789? an SSN? What about 098765432? Or 12345?"
        redactTestMsg = redactSsn(testMsg)
        self.assertEqual(
            redactTestMsg, 
            f"Is {self.SSN_REDACT}? an SSN? What about {self.SSN_REDACT}? Or 12345?"
        )
    
    def testRedactMessage(self):
        testMsg = "123456789 ssn, 1234567890 phone, abc@efg.com email"
        redactTestMsg = redactMessage(testMsg)
        self.assertEqual(
            redactTestMsg, 
            f"{self.SSN_REDACT} ssn, {self.PHONE_REDACT} phone, {self.EMAIL_REDACT} email"
        )

if __name__ == '__main__':
    unittest.main()