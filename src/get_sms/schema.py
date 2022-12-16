from pydantic import BaseModel

class date_sms(BaseModel):
    fromdate: str
    enddate: str