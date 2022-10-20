#Pydantic
from pydantic import BaseModel

class MobileNumbers(BaseModel): 
    mobileNumbers: str 

class VerificationCode(BaseModel):
    code: str