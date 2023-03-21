from fastapi import APIRouter
from schema.send_message_schema import MessageSchema
from config.db import engine
from model.messages import messages
from controller.controller_message import send_verify_number_phone



sms = APIRouter()

@sms.get("/")
def root():
    return {"hola mundo:" "Hola"}

#API para solicitar el numero de celular y enviar SMS

@sms.post("/send/sms")
def send_message(data_message: MessageSchema):
    messageSend = send_verify_number_phone(data_message.mobileNumber, data_message.apiKey, data_message.clientId)
    with engine.connect() as conn:
        conn.execute(messages.insert().values(messageSend[0]))
    return messageSend[1]

@sms.get("/get/sms")
def get_messages():
    with engine.connect() as conn:
        result = conn.execute(messages.select()).fetchall()
        print(result)
        return result
