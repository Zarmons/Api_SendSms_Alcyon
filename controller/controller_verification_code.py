import  secrets

# Validación para saber si el código ingresado si es igual al generado

def validate_verification_code():
    token = generate_token()
    response = {
            "token": f"{token}", 
            "response":"código valido" 
        }
    return response

# Creación de token 

def generate_token():
    token = secrets.token_urlsafe(50)
    return token