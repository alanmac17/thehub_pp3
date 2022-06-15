import gspread
from google.oauth2.service_account import Credentials
import pandas as pd
import numpy as np
import records

SCOPE = [
            "https://www.googleapis.com/auth/spreadsheets",
            "https://www.googleapis.com/auth/drive.file",
            "https://www.googleapis.com/auth/drive"
            ]
            
CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('the_hub')

database2 = SHEET.worksheet('courses')
courselisting = pd.DataFrame(database2.get_all_records())

def get_course(role):
        course_list = courselisting[(courselisting['description'].str.contains('role')) | (courselisting['course_title'].str.contains('role'))]
        print(course_list)



###test get_course with example
get_course('project manager')