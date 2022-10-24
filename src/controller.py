import requests
import json
import re
import random
import secrets
import asyncio

global global_code

# Validacion del numero celular y envio de SMS con en el codigo de validacion

def send_verify_number_phone(number):
    _REGEX_PHONE_NUMBER = re.compile(
        r"[(\+57|0057|57)?[ -]*(300|301|302|303|304|324|305|310|311|312|313|314|320|321|322|323|315|316|317|318|319|350|351|302|323|324|324|333|)[ -]*([0-9][ -]*){7}]"
    )
    if not _REGEX_PHONE_NUMBER.match(number):
        verification_code = create_verification_code()
        token = generate_token()
        url = "https://api.reddantu.com/api/v2/SendSMS"
        data = {
            "senderId": "sms",
            "message": "su codigo de validacion es: " f"{verification_code}",
            "mobileNumbers": number,
            "apiKey": "Rq1vExJtdTs/oZuUzHm0vYQNGO3ifyoNke53wxlxUr4=",
            "clientId": "64a8236c-ce6a-4f5a-abd1-a83ec221c7e7",
        }
        response_sms = requests.post(url, json=data)
        response = response_data( "success", "El codigo fue enviado correctamente al numero de celular: " f"{number}", f"{number}", f"{token}" )
    else:
        response = response_data( "error", "Por favor verifique su numero de celular", f"{number}", "null" )
    return response

# Creacion de codigos de seis digitos aleatoriamente

def create_verification_code():
    code_created = random.randint(100000, 999999)
    global global_code 
    global_code = code_created
    time = asyncio.sleep(60)
    if time == 0 :
        global_code = 0
    return code_created

# Validacion para saber si el codigo ingresado si es igual al generado

def validate_verification_code(verification_code):
    code = int(verification_code.code)
    if global_code == 0 :
        response = response_data("warning", "El tiempo ha caducado", f"{code}" " " f"{global_code}", "null")
    elif code != global_code :
        response = response_data("error", "verifica tu codigo", f"{code}" " " f"{global_code}", "null")
    else:
        response = response_data("success", "codigo valido", f"{code}" " " f"{global_code}", "null")
    return response

# Creacion de token 

def generate_token():
    token = secrets.token_urlsafe(50)
    return token

#Creacion de mensajes de respuesta de las API

def response_data(MessageDescription, Message, MobileNumber, token):
    response = {
        "Data": [
            {
                "MessageDescription": MessageDescription,
                "Message": Message,
                "MobileNumber": MobileNumber,
            }
        ],
        "AccessToken": token
    }
    return response
