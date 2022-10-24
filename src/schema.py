#Pydantic
from pydantic import BaseModel

class mobile_numbers(BaseModel): 
    mobileNumbers: str 

class verification_code(BaseModel):
    code: str