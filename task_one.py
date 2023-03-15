"""
----------------------
PROBLEM STATEMENT
----------------------

Write a program to get details of employees who's salary is > 9000.

"""

from typing import List

from my_utils.csvfile import HandleCSV


def do_task_one() -> List:
    reader = HandleCSV.read_entire_csv()
    emp_data = {}
    j = 1
    for i in reader:
        if int(i["SALARY"]) > 9000:
            emp_data[j] = {"Name": (i["FIRST_NAME"] + " " + i["LAST_NAME"]),
                      "email": i["EMAIL"], "Phone": i["PHONE_NUMBER"].replace(".", "")}
            j += 1
    return emp_data



if __name__ == "__main__":
    print(do_task_one())
