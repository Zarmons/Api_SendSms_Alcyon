#FastAPI
from fastapi import FastAPI

from src.controller import send_verify_number_phone
from src.schema import MobileNumbers

app = FastAPI()

@app.post("/sms", name="SMS")
def send_message(mobile_numbers: MobileNumbers):
    number = mobile_numbers.mobileNumbers
    message = send_verify_number_phone(number)
    return message