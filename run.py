import pandas as pd
import gspread
from google.oauth2.service_account import Credentials
import records
import content

SCOPE = [
            "https://www.googleapis.com/auth/spreadsheets",
            "https://www.googleapis.com/auth/drive.file",
            "https://www.googleapis.com/auth/drive"
            ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('the_hub_pp3')

database = SHEET.worksheet('reviews')
db = pd.DataFrame(database.get_all_records())

def add_review(employee_id):
    review_row = []

    print("Which review type would you like to enter?")
    print("'Training', 'Probation', 'Performance'")
    review_type = input("Select a review type from the list above: \n").lower()
    review_date = input("please insert the date of review: \n")
    reviewed_by = input("Please add first and last name of reviewer: \n")
    review_rating = input("Please add rating of 'pass' or 'fail': \n")
    review_notes = input("Please add any other relevant notes: \n")

    review_data = (employee_id, review_type, review_date, reviewed_by, review_rating, review_notes)
    review_row.append(review_data)

    print("Please confirm the following details entered are correct:\n")
    print("Thank you for your review, the details have now been entered on the hub\n")
    database.append_row(review_data)

def get_id():
    """
    Request user id, validate and return profile
    """
    while True:
        print("Please enter your an employee ID")
        print("Ids are 3 digit numbers - Example: 123\n")
            
        input_id = input("Enter the Employee ID here: \n")

        if validate_id(input_id):
            print(f"The code you entered was {input_id}")   
            break

    return input_id
            

def validate_id(values):
    """
    Check employee_id is 3 digits
    """
    try: 
        if len((values)) != 3:
            raise ValueError(
                f"An employee ID should be 3 numerical digits, you entered {(values)}"
            )
    
    except ValueError as e:
        print(f"That doesnt seem right {e}, please type a 3 digit employee id.\n")
        return False

    return True

def main_menu(employee_id):

    while True:
        employee_id = int(employee_id)
        records.EmployeeProfile(employee_id).get_profile()
       
        print("...")
        print("...")
        print("...")
        print("...")
        print("Select from the options below:")
        print("...")
        print("...")
        print("[1] to View the Employees Profile")
        print("[2] to Create a New Employee Profile")
        print("[3] to Leave an Employee Review")
        print("[4] to Get Recommended Courses")
        print("...")
        print("...")
        
        selection = int(input("Please enter a number between 1-4: "))

        if selection == 1:
            records.EmployeeProfile(employee_id).get_full_profile()
            main()
        elif selection == 2:
            records.add_employee()
            main()
        elif selection == 3:
            add_review(employee_id)
            main()
        elif selection == 4: 
            content.get_course(records.EmployeeProfile(employee_id).role)
            main()
        else:
            print("invalid entry")
            main()
                    
def main():
    """
    Call all functions 
    """
    print("Welcome to the employee onboarding Portal - The Hub")
    print("The Hub will provide you with the necessary steps to managing your human resources. \n")
    data = get_id()
    main_menu(data)

main()