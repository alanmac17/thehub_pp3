import gspread
from google.oauth2.service_account import Credentials
import pandas as pd


SCOPE = [
            "https://www.googleapis.com/auth/spreadsheets",
            "https://www.googleapis.com/auth/drive.file",
            "https://www.googleapis.com/auth/drive"
            ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('the_hub_pp3')

database3 = SHEET.worksheet('employees')
db3 = pd.DataFrame(database3.get_all_records())
db3.set_index('code', inplace=True)


class EmployeeProfile:
    """
    Employee profile object
    """
    def __init__(self, employee_id: str):
        employee = db3.loc[employee_id]

        self.first_name = employee.first_name
        self.last_name = employee.last_name
        self.email = employee.email_address
        self.role = employee.role
        self.start_date = employee.start_date
        self.salary = employee.salary
        self.line_manager = employee.line_manager
        self.department = employee.department
        self.employee_type = employee.employee_type


    def get_profile(self):
        """
        provide confirmation of id entered
        """
        print("Checking the ID in Employee Database...\n")
        print("...")
        print("...")
        print(f"You have selected {self.first_name} {self.last_name}")
        print(f"{self.role} in the {self.department} department")

    def get_full_profile(self):
        """
        provide full employee details
        """
        print(" \n Retrieving Data from Employee Database...\n")
        print(f" Name: {self.first_name} {self.last_name}")
        print(f" Department: {self.department}")
        print(f" Role: {self.role}")
        print(f" Start Date: {self.start_date}")
        print(f" Contact Email: {self.email}")
        print(f" Line Manager: {self.line_manager}")
        print(f" Department: {self.department}")
        print(f" Salary: {self.salary}")
        print(f" Employment Type: {self.employee_type}")


def add_employee():

    """
    Add an employee to the employee spreadsheet in google sheets
    """

    print("You have selected option 2 - Add an employee")
    print("Please complete all detail required for an employee : \n")
    new_code = "New"
    first_name = input("What is the employees first name: \n").lower()
    last_name = input("What is the employees last name: \n").lower()
    role = input("What is the employees role ex. Data Analyst: \n").lower()
    start_date = input("What date will the employee start: \n").lower()
    salary = input("What is the employees annual salary: \n").lower()
    line_manager = input("Who will be the employees line manager: \n").lower()
    department = input("Which department is the employee joining: \n").lower()
    email_address = input("What is the employees email address: \n").lower()
    employee_type = "New Hire"


    employees_row = [new_code, first_name, last_name, role, start_date, salary, line_manager, department, email_address, employee_type]
    print("Thank you, the details have now been entered on the hub")
    database3.append_row(employees_row)
