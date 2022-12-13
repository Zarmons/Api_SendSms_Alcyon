import requests, re, random, secrets

global global_code

# Validación del numero celular y envió de SMS con en el código de validación

def send_verify_number_phone(number):
    regex = r"^(\(?\+[\d]{1,3}\)?)\s?([\d]{1,5})\s?([\d][\s\.-]?){6,7}$"
    # regex = r"^(57)\s?(300|301|302|303|304|324|305|310|311|312|313|314|320|321|322|323|315|316|317|318|319|350|351|302|323|324|324|333)\s?([0-9]){7}$"
    result = re.match(regex, number)
    if result is None:
        response = response_data( "messageNumber", "error", "Por favor verifique su numero de celular", f"{number}", "null" )
    else:
        new_number = number.replace('+', '')
        verification_code = create_verification_code()
        url = "https://api.reddantu.com/api/v2/SendSMS"
        data = {
            "senderId": "sms",
            "message": "su código de validación es: " f"{verification_code}",
            "mobileNumbers": new_number,
            "apiKey": "Rq1vExJtdTs/oZuUzHm0vYQNGO3ifyoNke53wxlxUr4=",
            "clientId": "64a8236c-ce6a-4f5a-abd1-a83ec221c7e7",
            # "apiKey": "dl+FQ3GR1APhItJFV3YribLFH222STRBhM2KjrSauAU=",
            # "clientId": "03cd7ed3-a294-4daa-9350-76f92e99c7e6",
        }        
        response_sms = requests.post(url, json=data)
        print("sms--->",response_sms)
        # T = sms_trigger()
        response = response_data( "messageNumber", "success", "El código fue enviado al numero de celular: " f"{new_number}", f"{new_number}", "null" ), response_sms.request
    return  response

# Creación de códigos de seis dígitos aleatoriamente

def create_verification_code():
    code_created = random.randint(100000, 999999)
    global global_code 
    global_code = code_created
    return code_created

# Validación para saber si el código ingresado si es igual al generado

def validate_verification_code(verification_code):
    global global_code
    if  int(verification_code.code) != global_code :
        response = response_data("messageCode", "error", "Código invalido", "", "")
    else:
        token = generate_token()
        response = response_data("messageCode", "success", "Código valido", "", f"{token}")
        global_code = 0
    return response

# Creación de token 

def generate_token():
    token = secrets.token_urlsafe(50)
    return token

#Creación de mensajes de respuesta de las API

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