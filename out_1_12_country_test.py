import unittest
from out_1_12_country_pr import print_country as pc
class CountryTest(unittest.TestCase):
    def test_countrycity(self):
        allname=pc('beijing','china')
        self.assertEqual(allname,'beijing china')
    def test_countrycitypop(self):
        allname=pc('beijing','china',pop=2000000)
        self.assertEqual(allname,'beijing china population is 2000000')
unittest.main()