import unittest
import year

# test fonction year.py: validate_year()
y = year.validate_year(2021)
print(y)


class ValidateYearTestCase(unittest.TestCase):

    def test(self):
        y = year.validate_year('50')
        self.assertEqual(y, 1950)
        y = year.validate_year(1980)
        self.assertEqual(y, 1980)
        y = year.validate_year(13)
        self.assertEqual(y, 2013)
        y = year.validate_year(2021)
        self.assertEqual(y, 'trop grand !')
        y = year.validate_year('5jdm')
        self.assertEqual(y, None)


if __name__ == "__main__":
    unittest.main()
