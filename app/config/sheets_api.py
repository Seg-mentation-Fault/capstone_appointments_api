from __future__ import print_function

import os.path

from google.auth.transport.requests import Request
# from google.oauth2.credentials import Credentials
from google.oauth2.service_account import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# If modifying these scopes, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
SERVICE_ACCOUNT_FILE = './credentials.json'

def conect_spreadsheet():
    """Shows basic usage of the Sheets API.
    Prints values from a sample spreadsheet.
    """

    creds = Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes=SCOPES)

    return build('sheets', 'v4', credentials=creds)
