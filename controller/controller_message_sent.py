import requests, re, random, string

from controller.controller_apis_response import build_response_message_sent

# Validación del numero celular y envió de SMS con en el código de validación

def verify_number_send_message(mobileNumber):
    regex = r"^(\(?\+[\d]{1,3}\)?)\s?([\d]{1,5})\s?([\d][\s\.-]?){6,7}$"
    result = re.match(regex, mobileNumber)
    if result is None:
        dataResponse = {
            "replyTo": "messageError",
            "status": "Error",
            "response": "Por favor verifique el número de teléfono" 
        }
        response = build_response_message_sent( dataResponse )
    else:
        newMobileNumber = mobileNumber.replace('+', '')
        verificationCode = create_verification_code()
        messageId = create_message_id()
        url = "https://api.reddantu.com/api/v2/SendSMS"
        data = {
            "senderId": "sms",
            "message": "su codigo de validacion es: " f"{verificationCode}",
            "mobileNumbers": newMobileNumber,
            "apiKey": "Rq1vExJtdTs/oZuUzHm0vYQNGO3ifyoNke53wxlxUr4=",
            "clientId": "64a8236c-ce6a-4f5a-abd1-a83ec221c7e7",
        }        
        requests.post(url, json=data)
        dataResponse = {
            "replyTo": "messageSuccess",
            "message": f"{data['message']}", 
            "mobileNumber": f"{newMobileNumber}",
            "code": f"{verificationCode}",
            "status": "Success",
            "messageId": f"{messageId}",
            "response": "El código fue enviado al número de celular: " f"{newMobileNumber}" 
        }
        response = build_response_message_sent( dataResponse )
    return  response

# Creación de códigos de seis dígitos aleatoriamente

def create_verification_code():
    codeCreated = random.randint(100000, 999999)
    return codeCreated

# Creación de id de mensaje aleatoriamente

def create_message_id():
    messageIdCreated = ''.join([random.choice(string.ascii_letters + string.digits) for n in range(32)])
    return messageIdCreated
