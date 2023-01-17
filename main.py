#FastAPI
from fastapi import FastAPI, APIRouter
# from flask import Flask, request, Response

import redis

routes_product = APIRouter()
fake_db = []


#Archivos src
from src.sms_code.controller import send_verify_number_phone, validate_verification_code
from src.sms_code.schema import mobile_numbers, verification_code
from src.get_sms.controller import get_sms_sent
from src.get_sms.schema import  date_sms
from src.get_sms.crud import  save_hash, get_hash

app = FastAPI()

#API para solicitar el numero de celular y enviar SMS

@app.post("/sms", name="SMS")
def send_message(mobile_numbers: mobile_numbers):
    number = mobile_numbers.mobileNumbers
    response = send_verify_number_phone(number)
    return response

#API para verificar código generado

@app.post("/verification_code", name="VERIFICATION_CODE")
def validate_code(verification_code: verification_code):
    response = validate_verification_code(verification_code)
    return response

# Traer información de los sms enviados

@app.get("/list_message_date", name="LIST_MESSAGE_DATE")
def list_message(fromdate: str, enddate: str):
    response = get_sms_sent(fromdate, enddate)
    res = response["Data"]
    for i in range (len(res)):
        data = res[i]
        # OPERATION DB
        fake_db.append(data)

        # OPERATION CACHE
        save_hash(key=data["MessageId"], data=data)
    return "success", data


# Webhook para recibir sms enviados 1 por 1

# @app.post('/webhook')
# def return_response():
#     request: Request
    
#     response: Response._content
#     return response

# mostrar sms guardados con redis

@app.get("/list_message_db", name="LIST_MESSAGE_DB")
def list_message_db():
    info = 'prueba'
    data = get_hash(info)
    return data