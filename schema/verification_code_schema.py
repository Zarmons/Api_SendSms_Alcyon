from pydantic import BaseModel
from typing import Optional

class VerificationCodeSchema(BaseModel):
    messageId: str
    verificationCode: int

class ResponseVerificationCodeSchema(BaseModel):
    token: Optional[str]
    response: Optional[str]