import sys
import csv


class assessmentIPrice:

    def __init__(self, input_from_cmd):
        self.input_string = input_from_cmd

    def make_uppercase(self):
        # This method will return the uppercase string of the input string
        return self.input_string.upper()

    def make_lower_upper_alternating(self):
        # This method will modify the input string and return a string where first character is lowercase,
        # next character is uppercase and so on (alternating sequence)
        result_string = ""
        for index, char in enumerate(self.input_string):
            if index % 2 == 0:
                result_string = result_string + char.lower()
            else:
                result_string = result_string + char.upper()
        return result_string

    def create_csv(self):
        # This method takes an input string and writes each character in different column of first row of a
        # CSV file result.csv in the root path (same as this file).
        try:
            csv_file = open(file='result.csv', mode='w')
            wr = csv.writer(csv_file)
            wr.writerow(self.input_string)
            csv_file.close()
            return 'CSV created!'
        except PermissionError as e:
            # PermissionError will be thrown if the file is already open. Close the file and try to run the script again
            return 'Unable to create CSV. If result.csv is open, please close and try again later!'
        except Exception as e:
            # Generic exception
            return 'Unable to create CSV. Please try again later.'


if __name__ == "__main__":
    input_string = ' '.join(sys.argv[1:])
    obj = assessmentIPrice(input_string)
    print(obj.make_uppercase())
    print(obj.make_lower_upper_alternating())
    print(obj.create_csv())
