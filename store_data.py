# from openpyxl import load_workbook
import constants as const
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request


def update_excel(case_data, comment):

    excel_data = []
    excel_data.append(case_data['caseNumber'])
    excel_data.append(case_data['case_link'])
    excel_data.append(case_data['accountType'])
    excel_data.append(case_data['priority'])
    excel_data.append(case_data['subject'])
    excel_data.append(comment)

    creds = None
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file('./credentials/credentials.json', const.scopes)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    service = build('sheets', 'v4', credentials=creds)

    list = [excel_data]
    resource = {
        "majorDimension": "ROWS",
        "values": list
    }
    service.spreadsheets().values().append(
        spreadsheetId=const.spreadsheet_id,
        range=const.sheet_range,
        body=resource,
        valueInputOption="USER_ENTERED"
    ).execute()






