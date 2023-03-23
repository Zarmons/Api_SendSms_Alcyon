#Creación de mensajes de respuesta de las API

def  build_response_message_sent(dataResponse):
    if dataResponse["replyTo"] == "messageSuccess":
        response = {
            "messageId": dataResponse["messageId"],
            "message": dataResponse["message"],
            "mobileNumber": dataResponse["mobileNumber"],
            "code" : dataResponse["code"],
            "status": dataResponse["status"],
        }, {
            "messageId": dataResponse["messageId"],
            "responseMessage": dataResponse["response"]
        }
    else:
        response = {
            "status":dataResponse["status"],
        } , {
            "responseMessage": dataResponse["response"]
        }
    return response
   

    
