import unittest
from safe_harbor import birthDateToAge, dateToYear, stripZip

class TestSafeHarbor(unittest.TestCase):
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

        zipCodeLowPop = "10271"
        strippedZipLowPop = stripZip(zipCodeLowPop)
        self.assertEqual(strippedZipLowPop, "00000")


if __name__ == '__main__':
    unittest.main()