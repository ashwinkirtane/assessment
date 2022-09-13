import sys
import csv
from datetime import datetime
import os


class assessmentIPrice:

    def __init__(self, input_from_cmd):
        self.input_string = input_from_cmd

    @staticmethod
    def keep_latest_files():
        # When number of files are greater than 3 delete the oldest
        files = [f for f in os.listdir('.') if os.path.isfile(f) and f.endswith('.csv')]
        files.sort()
        # Get the first element of this list and delete
        if len(files) > 2:
            os.remove(files[0])
        return files

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
        self.keep_latest_files()
        ts_format = '%Y%m%d%H%M%S'
        ts = datetime.now().strftime(ts_format)
        filename = f'result-{str(ts)}.csv'
        result = {
            'filename': None,
            'text': None
        }
        try:
            csv_file = open(file=f'{filename}', mode='w')
            wr = csv.writer(csv_file)
            wr.writerow(self.input_string)
            csv_file.close()
            result['filename'] = filename
            result['text'] = 'CSV created!'
            return result
        except PermissionError as e:
            # PermissionError will be thrown if the file is already open. Close the file and try to run the script again
            result['text'] = 'Unable to create CSV. If result.csv is open, please close and try again later!'
            return result
        except Exception as e:
            # Generic exception
            result['text'] = 'Unable to create CSV. Please try again later.'
            return result


if __name__ == "__main__":
    input_string = ' '.join(sys.argv[1:])
    obj = assessmentIPrice(input_string)
    print(obj.make_uppercase())
    print(obj.make_lower_upper_alternating())
    print(obj.create_csv()['text'])
