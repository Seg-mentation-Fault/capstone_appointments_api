from pydantic import BaseModel
class AppointmentSchema(BaseModel):
    name: str
    phone: int
    document_type: str
    document_number: int
    email: str
    township: str
    eps: str
    requirement_type: str
    specialization_type: str
    coosalud_diagnostic: str
