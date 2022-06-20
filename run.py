
import gspread
from google.oauth2.service_account import Credentials
import pandas as pd
import numpy as np
import datetime
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
    print("1 for training review")
    print("2 for probation review")
    print("3 for performance review")
    review_type = input("Select a review type from 1-3: \n")
    review_date = input("please insert the date of review: \n")
    reviewed_by = input("Please add first and last name of reviewer: \n")
    review_rating = input("Please add rating of 'pass' or 'fail': \n")
    review_notes = input("Please add any other relevant notes: \n")

    review_row.append(review_type, review_date, reviewed_by, review_rating, review_notes)
    print(review_row)

def get_id():
    """
    Request employee id, validate and return profile
    """
    while True:
        print("Please enter an employee ID")
        print("Ids are 3 digit numbers - Example: 123\n")
            
        input_id = input("Enter Employee ID here: \n")

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

    employee_id = int(employee_id)
    records.EmployeeProfile(employee_id).get_profile()
    print("Select from the options below:")
    print("1 to View Full Employee Profile")
    print("2 to See Next Action")
    print("3 to Send Onboarding Email")
    print("4 to Get Recommended Courses")
    print("5 to Quit")

    selection = int(input("Select an option: "))
    
    if selection == 1:
        records.EmployeeProfile(employee_id).get_full_profile()
    elif selection == 2: 
        add_employee()
    elif selection == 3: 
        add_review(employee_id)
    elif selection == 4: 
        content.get_course(records.EmployeeProfile(employee_id).role)

def main():
    """
    Call all functions 
    """
    print("Welcome to your employee onboarding Portal - The Hub")
    print("The Hub will provide you with the necessary steps to set your employee up for success.")
    data = get_id()
    main_menu(data)

main()