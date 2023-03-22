from fastapi import APIRouter
from schema.send_message_schema import MessageSchema
from schema.verification_code_schema import VerificationCodeSchema
from config.db import engine
from model.messages import messages
from model.customers import customers
from controller.controller_message import verify_number_send_message, validate_verification_code

sms = APIRouter()

@sms.get("/")
def root():
    return {"API´s sms directos"}

#API para enviar mensajes con código de validación

@sms.post("/send/sms")
def send_message(dataMessage: MessageSchema):
    with engine.connect() as conn:
        client = conn.execute(customers.select().filter(customers.c.clientId == dataMessage.clientId).filter(customers.c.apiKey == dataMessage.apiKey)).first()
        if client:
            messageSend = verify_number_send_message(dataMessage.mobileNumber)
            if messageSend[0]["status"] == "Success":
                conn.execute(messages.insert().values(messageSend[0]))
                respuestaApi = messageSend[1]
            else:
                respuestaApi = messageSend[1]
        else:
            respuestaApi= "Por favor verifique sus credenciales"
    return respuestaApi

#API para traer los mensajes enviados

@sms.get("/get/sms", response_model=list[MessageSchema])
def get_messages():
    with engine.connect() as conn:
        result = conn.execute(messages.select()).fetchall()
        return result

# API para verificar código generado

@sms.post("/get/code")
def validate_code(dataVerification: VerificationCodeSchema):
    with engine.connect() as conn:
        code = conn.execute(messages.select().filter(messages.c.code == dataVerification.verificationCode).filter(messages.c.messageId == dataVerification.messageId)).first()
        if code:
            response = validate_verification_code()
        else:
             response = "código invalido"
    return response