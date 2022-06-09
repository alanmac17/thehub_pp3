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

def get_profile():
    """
    request employee number from user
    """
    print("Please enter an employee ID")
    print("Example: 123\n")

    Id = int(input("Enter Employee ID here: \n"))
    
    employee_id = db.loc[Id]

    print(f"Name: {employee_id.first_name} {employee_id.last_name}")
    print(f"Role: {employee_id.role}")
    print(f"Manager: {employee_id.line_manager}")
    print(f"Email: {employee_id.email_address}")
    print(f"Status: {employee_id.employee_type}")

def get_entitlements():
    """
    Work out employee benefits based on role, time
    """
    print("Please enter an employee ID")
    print("Example: 123\n")

    Id = int(input("Enter Employee ID here: \n"))

    def sabatical():
    ##employees are entitled to 1 month sabatical every 4 years worked
        employee_id = db.loc[Id]
        
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


def main():
    """
    menu to select a programme function
    """
    print("1 to View Employee Profile")
    print("2 to View Employee Entitlements")
    print("3 to Send Onboarding Email")
    print("4 to See Next Actions")
    print("5 to Quit")

    selection = int(input("Select an option: "))
    if selection == 1:
        get_profile()
    elif selection == 2:
        get_entitlements()
    elif selection == 3:
        send_email()
    elif selection == 4:
        send_email()
    elif selection == 5:
        sys.exit(0)
    else:
        print("Please select a number from the options listed")
        main()

print("Welcome to the Hub")
main()