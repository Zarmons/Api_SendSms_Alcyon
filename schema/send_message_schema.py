from pydantic import BaseModel
from typing import Optional

class MessageSchema(BaseModel):
    mobileNumber: str
    apiKey: str
    clientId: str

class ResponseMessageSchema(BaseModel):
    messageId: Optional[str]
    responseMessage: Optional[str]

class ResponseGetMessagesSchema(BaseModel):
    id:  str
    message: str
    mobileNumber: str
    code: int
    apiKey: str
    clientId: str
    status: str
