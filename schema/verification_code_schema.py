from pydantic import BaseModel
 
class VerificationCodeSchema(BaseModel):
    messageId: str
    verificationCode: int