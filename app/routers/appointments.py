from fastapi import APIRouter
from pydantic import BaseModel
from googleapiclient.errors import HttpError

from config.sheets_api import conect_spreadsheet

# The ID and range of a sample spreadsheet.
# SAMPLE_SPREADSHEET_ID = '1BxiMVs0XRA5nFMdKvBdBZjgmUUqptlbs74OgvE2upms'
SPREADSHEET_ID = '13BpK8bKhmqljT1M71V_nvWw-Vu2C6TuxThvJGJWsnhA'
RANGE_NAME = 'appointments_requests!A1:C1'

# How the input data should be interpreted.
VALUE_INPUT_OPTION = 'USER_ENTERED'  # TODO: Update placeholder value.

# How the input data should be inserted.
INSERT_DATA_OPTION = 'INSERT_ROWS'  # TODO: Update placeholder value.

router = APIRouter()

class AppointmentValues(BaseModel):
    name: str
    phone: int
    id: str

@router.get("/appointments", tags=["appointments"])
async def read_appointments():
    try:
        service = conect_spreadsheet()
        # Call the Sheets API
        sheet = service.spreadsheets()
        result = sheet.values().get(spreadsheetId=SPREADSHEET_ID,
                                    range=RANGE_NAME).execute()
        values = result.get('values', [])

        if not values:
            print('No data found.')
            return

        print('Name, Major:')
        for row in values:
            # Print columns A and E, which correspond to indices 0 and 4.
            print('%s, %s' % (row[0], row[4]))
    except HttpError as err:
        print(err)
    return [{"username": "Rick"}, {"username": "Morty"}]


@router.post("/appointments", tags=["appointments"])
async def create_appointments(appointment_value: AppointmentValues):

    data = [[appointment_value.name,appointment_value.phone,appointment_value.id]]
    try:
        service = conect_spreadsheet()
        # Call the Sheets API
        sheet = service.spreadsheets()
        result = sheet.values().append(spreadsheetId=SPREADSHEET_ID,
                                range=RANGE_NAME,
                                valueInputOption=VALUE_INPUT_OPTION,
                                insertDataOption=INSERT_DATA_OPTION,
                                body={"values":data}).execute()
        print(result)
        return result
    except HttpError as err:
        print(err)
