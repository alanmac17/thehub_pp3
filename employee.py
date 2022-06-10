import run.py

class EmployeeProfile:

    def __init__(self, employee_id: str):
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
        SHEET = GSPREAD_CLIENT.open('the_hub')

        database = SHEET.worksheet('employees')
        db = pd.DataFrame(database.get_all_records())
        db.set_index('code', inplace=True)
        print(db.head())

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

    