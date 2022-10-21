#Pydantic
from lib2to3.pytree import Base
from pydantic import BaseModel

class mobile_numbers(BaseModel): 
    mobileNumbers: str 

class verification_code(BaseModel):
    code: str
