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


database2 = SHEET.worksheet('courses')
courselisting = pd.DataFrame(database2.get_all_records())

def get_course(role):
    course_list=courselisting['description'].str.lower().isin(role)
    print(course_list)


###test get_course with example
get_course('data analyst')