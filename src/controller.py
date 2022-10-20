import requests
import json
import re
import random

# Validacion del numero celular y envio de SMS con en el codigo de validacion

def send_verify_number_phone(number):
    _REGEX_PHONE_NUMBER = re.compile(r'[(\+57|0057|57)?[ -]*(300|301|302|303|304|324|305|310|311|312|313|314|320|321|322|323|315|316|317|318|319|350|351|302|323|324|324|333|)[ -]*([0-9][ -]*){7}]')
    if not _REGEX_PHONE_NUMBER.match(number):
        verification_code = create_verification_code()
        url = 'https://api.reddantu.com/api/v2/SendSMS'
        data = {
            'senderId': 'sms',
            'message':  'su codigo de validacion es: ' f'{verification_code}',
            'mobileNumbers': number,
            'apiKey': 'Rq1vExJtdTs/oZuUzHm0vYQNGO3ifyoNke53wxlxUr4=',
            'clientId': '64a8236c-ce6a-4f5a-abd1-a83ec221c7e7'
        }
        response = requests.post(url, json=data)
        message = 'El codigo fue enviado correctamente al numero de celular: ' f'{number}'
    else :
        message = 'Por favor verifique su numero de celular'
    return message

# Creacion de codigos de seis digitos aleatoriamente

def create_verification_code():
    code_created = random.randint(100000, 999999)
    return code_created

# Validacion para saber si el codigo ingresado si es igual al generado

def validate_verification_code(code):
    if code == "123456" :
        message = 'codigo valido'
    else :
        message = 'verifica tu codigo'
    return message


