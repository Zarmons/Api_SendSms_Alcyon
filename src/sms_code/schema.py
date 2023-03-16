#Pydantic
from pydantic import BaseModel

class mobile_numbers(BaseModel): 
    mobileNumbers: str 
    apiKey: str
    clientId: str

class verification_code(BaseModel):
    code: str