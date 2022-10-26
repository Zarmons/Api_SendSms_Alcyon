import requests, re, random, secrets

global global_code

# Validacion del numero celular y envio de SMS con en el codigo de validacion

def send_verify_number_phone(number):
    regex = r"^(\(?\+[\d]{1,4}\)?)\s?([\d]{1,5})\s?([\d][\s\.-]?){6,10}$"
    result = re.match(regex, number)
    if result is None:
        response = response_data( "messageNumber", "error", "Por favor verifique su numero de celular", f"{number}", "null" )
    else:
        verification_code = create_verification_code()
        url = "https://api.reddantu.com/api/v2/SendSMS"
        data = {
            "senderId": "sms",
            "message": "su codigo de validacion es: " f"{verification_code}",
            "mobileNumbers": number,
            "apiKey": "Rq1vExJtdTs/oZuUzHm0vYQNGO3ifyoNke53wxlxUr4=",
            "clientId": "64a8236c-ce6a-4f5a-abd1-a83ec221c7e7",
        }        
        response_sms = requests.post(url, json=data)
        response = response_data( "messageNumber", "success", "El codigo fue enviado correctamente al numero de celular: " f"{number}", f"{number}", "null" )
    return response

# Creacion de codigos de seis digitos aleatoriamente

def create_verification_code():
    code_created = random.randint(100000, 999999)
    global global_code 
    global_code = code_created
    return code_created

# Validacion para saber si el codigo ingresado si es igual al generado

def validate_verification_code(verification_code):
    global global_code
    if  int(verification_code.code) != global_code :
        response = response_data("messageCode", "error", "verifica tu codigo", "", "")
    else:
        token = generate_token()
        response = response_data("messageCode", "success", "codigo valido", "", f"{token}")
        global_code = 0
    return response

# Creacion de token 

def generate_token():
    token = secrets.token_urlsafe(50)
    return token

#Creacion de mensajes de respuesta de las API

def response_data(typeMessage, MessageDescription, Message, MobileNumber, token):
    if typeMessage == "messageNumber" :
        response = {
            "Data": [
                {
                    "MessageDescription": MessageDescription,
                    "Message": Message,
                    "MobileNumber": MobileNumber,
                }
            ]
        }
    else:
        response = {
            "Data": [
                {
                    "MessageDescription": MessageDescription,
                    "Message": Message,
                }
            ],
            "AccessToken": token
        } 
    return response