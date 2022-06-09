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

employees = SHEET.worksheet('employees')
df = pd.DataFrame(employees.get_all_records())
print(df.head())


def request_employee_number():
    """
    request employee number from user
    """
    print("Please enter an employee number")
    print("Data should be three numbers.")
    print("Example: 123\n")
        
    employee_code = int(input("Enter here: \n"))
    results = df.loc[df['code'] == employee_code]
    print(results)

request_employee_number()

# def create_employee_benefits()
# """
# Work out employee benefits based on role, time
# """

# def employee_next_action()
# """
# Work out the next appropriate action for employee
# """

# def get_training_material()
# """
# linkedin learning API and retrive training course data based on role
# """

# def get_latest_social_feeds()
# """
# Access company social sites and retrive latest posts
# """

# def format_onboarding_email()
# """
# format onboarding email with content from benefits, actions, material, social feeds
# """

# def send_email()
# """
# send email to employee and hiring manager
# """


# def main():
#     """
#     Run all program functions
#     """
#     get_employee()

# print("Welcome to the Hub")
# main()