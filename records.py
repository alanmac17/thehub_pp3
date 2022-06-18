import gspread
from google.oauth2.service_account import Credentials
import pandas as pd
import numpy as np

SCOPE = [
            "https://www.googleapis.com/auth/spreadsheets",
            "https://www.googleapis.com/auth/drive.file",
            "https://www.googleapis.com/auth/drive"
            ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('the_hub_pp3')

database = SHEET.worksheet('employees')
db = pd.DataFrame(database.get_all_records())
db.set_index('code', inplace=True)

class EmployeeProfile:
    """
    Employee profile object 
    """
    def __init__(self, employee_id: str):
        employee = db.loc[employee_id]
        
        self.first_name = employee.first_name
        self.last_name = employee.last_name
        self.email = employee.email_address
        self.role = employee.role
        self.start_date = employee.start_date
        self.salary = employee.salary
        self.line_manager = employee.line_manager
        self.department = employee.department
        self.employee_type = employee.employee_type
        self.onboarded = employee.onboarded
        self.three_month_checkin_email = employee.three_month_checkin_email
        self.six_month_eval_email = employee.six_month_eval_email
        self.pass_probation = employee.pass_probation

    def get_profile(self):
        """
        provide brief employee details
        """

        print(" \n Retrieving Data from Employee Database...\n")
        print(f" Name: {self.first_name} {self.last_name}")
        print(f" Department: {self.department}")
        print(f" Role: {self.role}")
        print(f" Start Date: {self.start_date}")
        print(f" Onboarding Complete: {self.onboarded}")

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
        print(f" Onboarding Complete: {self.onboarded}")
        print(f" 3 Month Checkin Email Sent: {self.three_month_checkin_email}")
        print(f" 6 Month Evaluation Email Sent: {self.six_month_eval_email}")
        print(f" Probation Passed: {self.pass_probation}")


## test get_profile() ###
# print('\n Testing get profile call')
# EmployeeProfile(102).get_profile()
# EmployeeProfile(102).get_full_profile()