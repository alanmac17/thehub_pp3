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
SHEET = GSPREAD_CLIENT.open('the_hub_pp3')

database2 = SHEET.worksheet('courses')
courselisting = pd.DataFrame(database2.get_all_records())

def get_course(role):
        print(f"The follow courses are recommeneded for {role}:")
        results = courselisting[(courselisting['description'].str.contains(role)) | (courselisting['course_title'].str.contains(role))]
        top_five_results = results.iloc[:5,] 
        print(top_five_results[["course_id", "description"]])

# ###test get_course with example
get_course('project manager')