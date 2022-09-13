## About
This is the solution to the assessment provided as part of the iPrice recruitment process. The assessment question is part of this repo in a PDF file.

## Prerequisites
You would need Python. Although this is built on version 3.10 but since it does not use any libraries specific to version 3.X.X, this should work on Python 2.X.X also.

## Getting Started
It is pretty simple to run this. Simply go to the root folder containing the assessment_iprice.py file and run this command on the command prompt:
```sh
  python assessment_iprice.py <<string_to_test>>
```
In the <<string_to_test>> place the string value that you need to test on (without the angular brackets). <br/>
Please note that if result.csv is already open, the CSV creation will not happen.

## Analysing Result
You should get 3 lines of output on the command. 
1. The first line should be the input string in uppercase. 
2. Second line should be the input string alternating between lowercase and uppercase. 
3. The third line would print "CSV created!" if the given string has been successfully written into the CSV file. The resulting CSV file would be created on the same path with the name *result.csv.* In case there is an error in creating the CSV file, you would get an output as "Unable to create CSV. Please try again later."   