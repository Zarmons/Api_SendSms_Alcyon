#FastAPI
from fastapi import FastAPI

#Archivos src
from src.sms_code.controller import send_verify_number_phone, validate_verification_code
from src.sms_code.schema import mobile_numbers, verification_code
from src.get_sms.controller import get_sms_sent

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

@app.get("/list_message", name="LIST_MESSAGE")
def list_message():
    response = get_sms_sent()
    return response