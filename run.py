import pandas as pd
import gspread
from google.oauth2.service_account import Credentials
import records

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

database2 = SHEET.worksheet('courses')
courselisting = pd.DataFrame(database2.get_all_records())

def get_course(role):
        """
        Retrieve courses that are related to the employee role from the courses google spreadsheet
        """
        print(f"The follow courses are recommeneded for {role}:")
        results = courselisting[(courselisting['description'].str.contains(role)) | (courselisting['course_title'].str.contains(role))]
        top_ten_results = results.iloc[:10,] 
        print(top_ten_results[["course_id", "description"]])
        print(...)
        print(...)

def add_review(employee_id):
    """
    Input a review, passing the employee id and append to the reviews google sheet 
    """
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

def next_action(employee_id):
    """
    Retrieve the next action by passing the employee id and filtering the review sheet 
    """
    pass_list = db.loc[db['rating'] == 'pass'and db['code'] == employee_id]
        
    print(pass_list)

    result = []
    for value in pass_list["review_type"]:
        if value == 'probation':
            result.append("performance review")
        elif value == 'training':
            result.append("probation review")
        else:
            result.append("training review")
       
    print(f"The recommended action for employee {records.EmployeeProfile(employee_id).first_name} is {result}")
    print(...)
    print(...)  

def get_id():
    """
    Request user id, validate and return profile
    """
    while True:
        print("Please enter an employee ID")
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
    """
    Menu options for the user to select from
    """
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
        print("[2] to Get Recommended Courses")
        print("[3] to Leave an Employee Review")
        print("[4] to Get Recommended Next Action")
        print("[5] to Create a New Employee Profile")
        print("...")
        print("...")
        
        selection = int(input("Please enter a number between 1-5: "))

        if selection == 1:
            records.EmployeeProfile(employee_id).get_full_profile()
            main()
        elif selection == 2: 
            get_course(records.EmployeeProfile(employee_id).role)
            main()
        elif selection == 3:
            add_review(employee_id)
            main()
        elif selection == 4: 
            next_action(employee_id)
            main()
        elif selection == 5:
            records.add_employee()
            main()
        else:
            print("invalid entry")
            main()
                    
def main():
    """
    Call all functions 
    """
    print("Welcome to the employee onboarding Portal - The Hub")
    print("The Hub will provide you with the necessary steps to manage your human resources. \n")
    print("TYou will have the option of viewing employee details, adding new employees and much more. \n")
    print("As with any system we hope to continually develop new and useful features. \n")
    print("Please email get the.hub.pp3@gmail.com with any suggestions or feedback. \n")
    data = get_id()
    main_menu(data)

main()