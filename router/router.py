from fastapi import APIRouter
from schema.send_message_schema import MessageSchema, ResponseMessageSchema, ResponseGetMessagesSchema
from schema.verification_code_schema import VerificationCodeSchema, ResponseVerificationCodeSchema
from config.db import engine
from model.messages import messages
from model.users import users
from controller.controller_message_sent import verify_number_send_message
from controller.controller_verification_code import validate_verification_code

sms = APIRouter()

@sms.get("/")
def root():
    return {"API´s sms directos"}

#API para enviar mensajes con código de validación

@sms.post("/post/send", response_model=ResponseMessageSchema)
def send_message(dataMessage: MessageSchema):
    with engine.connect() as conn:
        credentials = conn.execute(users.select().filter(users.c.user_clientId == dataMessage.clientId).filter(users.c.user_apiKey == dataMessage.apiKey).filter(users.c.user_status == "ACTIVE")).first()
        if credentials:
            messageSent = verify_number_send_message(dataMessage.mobileNumber)
            if messageSent[0]["status"] == "Success":
                conn.execute(messages.insert().values(messageSent[0]))
                responseApi = messageSent[1]
            else:
                responseApi = messageSent[1]
        else:
            responseApi= {"responseMessage": "Por favor verifique sus credenciales"}
    return responseApi

#API para traer los mensajes enviados

@sms.get("/get/sms", response_model=list[ResponseGetMessagesSchema] )
def get_messages():
    with engine.connect() as conn:
        result = conn.execute(messages.select()).fetchall()
    return result

# API para verificar código generado

@sms.post("/post/validate", response_model=ResponseVerificationCodeSchema)
def validate_code(dataVerification: VerificationCodeSchema):
    with engine.connect() as conn:
        code = conn.execute(messages.select().filter(messages.c.code == dataVerification.verificationCode).filter(messages.c.messageId == dataVerification.messageId)).first()
        if code:
            response = validate_verification_code()
        else:
            response = {"response":"código invalido"}
    return response