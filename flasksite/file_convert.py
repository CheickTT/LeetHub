import csv
import os
script_dir = os.path.dirname(__file__)
# returns alphabetized array of all colleges in the US
# read from csv file
def get_college_list():
    colleges = []
    abs_path = os.path.join(script_dir, 'list_of_us_colleges.csv')
    with open(abs_path, newline='') as uni_list:
        reader = csv.reader(uni_list, delimiter=',')
        next(reader)
        for line in reader:
            colleges.append(line[1])
    colleges.sort(key=str.lower)
    return colleges

