"""
----------------------
PROBLEM STATEMENT
----------------------

Write a program to get "HIRE DATE" of employee who's department is within range 30
to 110 AND who's salary is > 4200.

"""

from typing import Dict


from my_utils.csvfile import HandleCSV
from my_utils.date_converter import convert_date


def do_task_two() -> Dict:
    """ Returns dict object data containing 'HIRE DATE' and 'NAME' from given csv file"""

    reader = HandleCSV.read_entire_csv()
    getdata = {}
    for data in reader:
        if 30 < int(data.get("DEPARTMENT_ID")) < 110 and int(data.get("SALARY")) > 4200:
            date = convert_date(data['HIRE_DATE'])
            getdata.setdefault(date, []).extend([data.get('FIRST_NAME') + " " + data.get('LAST_NAME')])
    return getdata


if __name__ == "__main__":
    print(do_task_two())


