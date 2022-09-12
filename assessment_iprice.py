import sys
import csv


class assessmentIPrice:

    def __init__(self, input_from_cmd):
        self.input_string = input_from_cmd

    def make_uppercase(self):
        return self.input_string.upper()

    def make_lower_upper_alternating(self):
        result_string = ""
        for index, char in enumerate(self.input_string):
            if index % 2 == 0:
                result_string = result_string + char.lower()
            else:
                result_string = result_string + char.upper()
        return result_string

    def create_csv(self):
        try:
            csv_file = open(file='result.csv', mode='w')
            wr = csv.writer(csv_file)
            wr.writerow(self.input_string)
            csv_file.close()
            return 'CSV created!'
        except PermissionError as e:
            return 'Unable to create CSV. If result.csv is open, please close and try again later!'
        except Exception as e:
            return 'Unable to create CSV. Please try again later.'


if __name__ == "__main__":
    input_string = ' '.join(sys.argv[1:])
    obj = assessmentIPrice(input_string)
    print(obj.make_uppercase())
    print(obj.make_lower_upper_alternating())
    print(obj.create_csv())
