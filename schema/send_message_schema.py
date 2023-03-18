from pydantic import BaseModel
from typing import Optional
 
class MessageSchema(BaseModel):
    # id:  Optional[str]
    # message: str
    mobileNumber: str
    # code: int
    apiKey: str
    clientId: str
    # status: str