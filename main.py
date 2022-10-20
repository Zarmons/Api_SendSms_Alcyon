#FastAPI
from fastapi import FastAPI

#Archivos src
from src.controller import send_verify_number_phone, validate_verification_code
from src.schema import MobileNumbers, VerificationCode

app = FastAPI()

#API para solicitar el numero de celular y enviar SMS

@app.post("/sms", name="SMS")
def send_message(mobile_numbers: MobileNumbers):
    number = mobile_numbers.mobileNumbers
    response = send_verify_number_phone(number)
    return response

#API para verificar codigo generado

@app.post("/verification_code", name="VERIFICATION_CODE")
def validate_code(verification_code: VerificationCode):
    code = verification_code.code
    response = validate_verification_code(code)
    return response