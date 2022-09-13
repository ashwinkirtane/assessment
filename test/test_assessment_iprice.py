from unittest import TestCase
from assessment_iprice import assessmentIPrice
import csv
import os


class AssessmentTestCases(TestCase):
    def test_upper_case(self):
        lower_string = "abcdefgh"
        obj = assessmentIPrice(lower_string)
        r = obj.make_uppercase()
        self.assertTrue(r.isupper())

    def test_lower_upper_case(self):
        res = True
        lower_string = "abcdefgh"
        obj = assessmentIPrice(lower_string)
        r = obj.make_lower_upper_alternating()
        for i, c in enumerate(r):
            if i % 2 == 0 and not c.islower():
                res = False
            elif i % 2 != 0 and not c.isupper():
                res = False
        self.assertTrue(res)

    def test_correct_csv(self):
        # A test_csv is present in the test folder which should be the result from the string - "hello this is Testing!"
        # We will be reading this CSV and asserting whether this is indeed the string
        string_to_compare = "hello this is Testing!"
        with open('test_csv.csv', newline='') as f:
            reader = csv.reader(f)
            row1 = next(reader)
            string_from_csv = ''.join(map(str, row1))
            self.assertTrue(string_from_csv == string_to_compare)

    def test_create_csv_and_test(self):
        s = "hello this is Testing 123!"
        obj = assessmentIPrice(s)
        r = obj.create_csv()
        # This has created a file - now we need to read this CSV and compare it with above string
        with open(f'{r["filename"]}', newline='') as f:
            reader = csv.reader(f)
            row1 = next(reader)
            string_from_csv = ''.join(map(str, row1))
        os.remove(f"{r['filename']}")
        self.assertTrue(string_from_csv == s)

    def test_random_characters1(self):
        s = "*(&*#@^$120930921437&*@#*@!@#(@!#*"
        # This should return the same string from all 3 methods
        obj = assessmentIPrice(s)
        r = obj.make_uppercase()
        self.assertTrue(r == s)

    def test_random_characters2(self):
        s = "*(&*#@^$120930921437&*@#*@!@#(@!#*"
        # This should return the same string from all 3 methods
        obj = assessmentIPrice(s)
        r = obj.make_lower_upper_alternating()
        self.assertTrue(r == s)

    def test_random_characters3(self):
        s = "*(&*#@^$120930921437&*@#*@!@#(@!#*"
        # This should return the same string from all 3 methods
        obj = assessmentIPrice(s)
        r = obj.create_csv()
        # CSV created after this step
        if r['text'] == 'CSV created!':
            with open(f'{r["filename"]}', newline='') as f:
                reader = csv.reader(f)
                row1 = next(reader)
                string_from_csv = ''.join(map(str, row1))
            os.remove(f'{r["filename"]}')
            self.assertTrue(string_from_csv == s)
