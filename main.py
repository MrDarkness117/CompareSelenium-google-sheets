from googleapiclient.discovery import build
from google.oauth2 import service_account
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
import os

SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
SERVICE_ACCOUNT_FILE = 'keys.json'

creds = None
creds = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, scopes=SCOPES)

# The ID and range of a sample spreadsheet.
SAMPLE_SPREADSHEET_ID = '1l2WwHpmTKPwChWJKckbCiOG0wzFUHDI5ypqqY0QRYU4'

service = build('sheets', 'v4', credentials=creds)

# Call the Sheets API
sheet = service.spreadsheets()
result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                            range="blinks!A1:B1054").execute()
values = result.get('values', [])

print(values)

driver = webdriver.Chrome()
driver.implicitly_wait(0.5)

log = ''
line = 0

for pair in values:
    driver.get(pair[0])
    link = pair[1][20:]
    line += 1
    try:
        driver.find_element_by_xpath("//*[contains(@href, '{}')]".format(link))
        report = 'На странице ' + pair[0] + ' найдена битая ссылка: ' + pair[1] + '\n'
        print(report)
        log += report
    except:
        print("Строка №" + str(line) + " прошла")


if not os.path.exists('./report.txt'):
    with open('report.txt', 'w') as report:
        report.write(log)


# if __name__ == '__main__':
#     main()
