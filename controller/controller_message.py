import requests, re, random, secrets, string

global global_code

# Validación del numero celular y envió de SMS con en el código de validación

def verify_number_send_message(mobileNumber):
    regex = r"^(\(?\+[\d]{1,3}\)?)\s?([\d]{1,5})\s?([\d][\s\.-]?){6,7}$"
    # regex = r"^(57)\s?(300|301|302|303|304|324|305|310|311|312|313|314|320|321|322|323|315|316|317|318|319|350|351|302|323|324|324|333)\s?([0-9]){7}$"
    result = re.match(regex, mobileNumber)
    if result is None:
        response = response_data( "null", "null", "null", "Error", "null", "Por favor verifique el número de teléfono" )
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
        response = response_data( f"{data['message']}", f"{newMobileNumber}", f"{verificationCode}", "Success", f"{messageId}", "El código fue enviado al número de celular: " f"{newMobileNumber}" )
    return  response

# Creación de códigos de seis dígitos aleatoriamente

def create_verification_code():
    codeCreated = random.randint(100000, 999999)
    return codeCreated

# Creación de id de mensaje aleatoriamente

def create_message_id():
    messageIdCreated = ''.join([random.choice(string.ascii_letters + string.digits) for n in range(32)])
    return messageIdCreated




# Validación para saber si el código ingresado si es igual al generado

def validate_verification_code():
    token = generate_token()
    response = response_data("", "", "", "Success", f"{token}", "Código valido")
    return response

# Creación de token 

def generate_token():
    token = secrets.token_urlsafe(50)
    return token





#Creación de mensajes de respuesta de las API

def response_data(messageSend, mobileNumber, code, messageStatus, token, responseMessage,):
    if messageStatus == "Success" :
        response = {
            "messageId": token,
            "message": messageSend,
            "mobileNumber": mobileNumber,
            "code" : code,
            "status": messageStatus,
        }, {
            "messageId": token,
            "responseMessage": responseMessage
        }
    else:
        response = {
            "status": messageStatus,
        } , {
            "responseMessage": responseMessage
        }
    return response

# rootsms
# Sdgf45sdf#10Za8edx

# database-sms.cmyoanwvm7px.us-east-2.rds.amazonaws.com://rootsms:Sdgf45sdf#10Za8edx@localhost:3306/sms
