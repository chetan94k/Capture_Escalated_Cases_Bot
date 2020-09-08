# Login
username = ''
password = b''
security_token = b''

# SOQL
query = "SELECT CaseNumber,Subject,Id,Priority,Account_Type__c  FROM Case  WHERE  CaseNumber='"
case_permalink = 'https://uipath.lightning.force.com/lightning/r/Case/{0}/view'
headers = {"Content-Type": "application/json", "Accept": "application/json"}

# Excel details
file_path = "./output/test.xlsx"

# google_sheet
scopes = ['https://www.googleapis.com/auth/spreadsheets']
spreadsheet_id = '1jJBJeh8_oreez1dd_fM-BEKsH9gjEdCkKtLuDxqOJEM'
sheet_range = 'Sheet1!A:A'