import records
import content
     

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

    print("1 to View Full Employee Profile")
    print("2 to See Next Action")
    print("3 to Send Onboarding Email")
    print("4 to Get Recommended Courses")
    print("5 to Quit")

    selection = int(input("Select an option: "))
    
    if selection == 1:
        records.EmployeeProfile(employee_id).get_full_profile()
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