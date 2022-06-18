import gspread
from google.oauth2.service_account import Credentials
import pandas as pd
import numpy as np
import datetime

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

today = date.today()


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
        self.pass_probation = employee.pass_probation
        self.last_review_date = employee.last_review_date
        self.next_review_date = employee.next_review_date
        self.next_review_type = employee.next_review_type

    def get_profile(self):
        """
        provide brief employee details
        """
        print(" \n Retrieving Data from Employee Database...\n")
        print(f" Name: {self.first_name} {self.last_name}")
        print(f" Department: {self.department}")
        print(f" Role: {self.role}")
        print(f" Start Date: {self.start_date}")
        print(f" Employment Type: {self.employee_type}")

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
        print(f" Probation Passed: {self.pass_probation}")
        print(f" Last Review Date: {self.last_review_date}")
        print(f" Next Review Date: {self.next_review_date}")
        print(f" Next Review Date: {self.next_review_type}")
    
    def onboard_new_hires()
        """
        Gather all new hires that are due to start next week 
        """
        if employee.start_date <= 


## test get_profile() ###
# print('\n Testing get profile call')
# EmployeeProfile(102).get_profile()
# EmployeeProfile(102).get_full_profile()