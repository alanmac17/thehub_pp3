import records
import content

def main():

    """
    request employee number from user
    """
    print("Please enter an employee ID")
    print("Example: 123\n")

    employee_id = (int(input("Enter Employee ID here: \n")))
    
    print("1 to View Employee Profile")
    print("2 to View Entitlements")
    print("3 to Send Onboarding Email")
    print("4 to See Next Actions")
    print("5 to Quit")

    selection = int((input("Select an option: ")))
    
    if selection == 1:
        records.EmployeeProfile(employee_id).get_profile()
    elif selection == 4: 
        content.get_course(records.EmployeeProfile(employee_id).role)

print("Welcome to the Hub")
main()