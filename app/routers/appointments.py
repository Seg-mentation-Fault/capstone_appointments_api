from schemas.appointents_schema import AppointmentSchema
import sys

from config.sheets_api import conect_spreadsheet
from fastapi import APIRouter
from googleapiclient.errors import HttpError

sys.path.append("..")


# The ID and range of a sample spreadsheet.
# SAMPLE_SPREADSHEET_ID = '1BxiMVs0XRA5nFMdKvBdBZjgmUUqptlbs74OgvE2upms'
SPREADSHEET_ID = '13BpK8bKhmqljT1M71V_nvWw-Vu2C6TuxThvJGJWsnhA'
RANGE_NAME = 'appointments_requests!A1:J1'

# How the input data should be interpreted.
VALUE_INPUT_OPTION = 'USER_ENTERED'  # TODO: Update placeholder value.

# How the input data should be inserted.
INSERT_DATA_OPTION = 'INSERT_ROWS'  # TODO: Update placeholder value.

router = APIRouter()


@router.get("/appointments/{document_id}", tags=["appointments"])
async def read_appointments(document_id):
    filter = {}
    try:
        service = conect_spreadsheet()
        # Call the Sheets API
        sheet = service.spreadsheets()
        result = sheet.values().get(spreadsheetId=SPREADSHEET_ID,
                                    range='appointments_requests!A2:L').execute()
        values = result.get('values', [])

        if not values:
            print('No data found.')
            return
        for row in values:
            if row[3] == document_id:
                filter[row[0]] = {
                    "document_number": row[3],
                    "requirement_type": row[7],
                    "status": row[10]
                }
    except HttpError as err:
        print(err)
    return filter


@router.post("/appointments", tags=["appointments"])
async def create_appointments(body: AppointmentSchema):

    data = [[
        body.name,
        body.phone,
        body.document_type,
        body.document_number,
        body.email,
        body.township,
        body.eps,
        body.requirement_type,
        body.specialization_type,
        body.coosalud_diagnostic,
        'Pendiente',
        body.platform
    ]]

    try:
        service = conect_spreadsheet()
        # Call the Sheets API
        sheet = service.spreadsheets()
        result = sheet.values().append(spreadsheetId=SPREADSHEET_ID,
                                       range=RANGE_NAME,
                                       valueInputOption=VALUE_INPUT_OPTION,
                                       insertDataOption=INSERT_DATA_OPTION,
                                       body={"values": data}).execute()
        print(result)
        return result
    except HttpError as err:
        print(err)
