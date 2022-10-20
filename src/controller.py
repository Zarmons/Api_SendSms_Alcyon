import requests
import json

def send_verify_number_phone(number):
    length_number = len(number)
    if  length_number == 12 :
        url = 'https://api.reddantu.com/api/v2/SendSMS'
        data = {
            'senderId': 'sms',
            'message':  'su codigo de validacion es: ' f'12345',
            'mobileNumbers': number,
            'apiKey': 'Rq1vExJtdTs/oZuUzHm0vYQNGO3ifyoNke53wxlxUr4=',
            'clientId': '64a8236c-ce6a-4f5a-abd1-a83ec221c7e7'
        }
        response = requests.post(url, json=data)
        message = 'El codigo fue enviado correctamente al numero de celular: ' f'{number}'
    else :
        message = 'El Numero no es valido'

    return message