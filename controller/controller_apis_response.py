#Creación de mensajes de respuesta de las API

def  build_response(dataResponse):
    print(dataResponse)
    replyToo: dataResponse["replyTo"]
    switch_build_response =  {
        1:messageSuccess(dataResponse),
        2:messageError(dataResponse),
    }  
    switch_build_response.get(replyToo)()
def messageSuccess(dataResponse):
    print("-->",dataResponse["messageId"])
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
    return response
def messageError(dataResponse):   
    response = {
        "status":dataResponse["status"],
    } , {
        "responseMessage": dataResponse["response"]
    }
    return response
   

    
