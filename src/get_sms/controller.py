import requests

from datetime import datetime


def get_sms_sent():
    data= {
        'fromdate' : datetime.today(),
        'enddate' : datetime.today(),
        'start' : 1,
        'length' : 10000000,
        'ApiKey' : 'Rq1vExJtdTs/oZuUzHm0vYQNGO3ifyoNke53wxlxUr4=',
        'ClientId' : '64a8236c-ce6a-4f5a-abd1-a83ec221c7e7'
        # apiKey: dl+FQ3GR1APhItJFV3YribLFH222STRBhM2KjrSauAU=
        # clientId: 03cd7ed3-a294-4daa-9350-76f92e99c7e6
    }
    
    url = "https://api.reddantu.com/api/v2/GetSMS"
    # url= "https://api.reddantu.com/api/v2/GetSMS?ApiKey=Rq1vExJtdTs/oZuUzHm0vYQNGO3ifyoNke53wxlxUr4=&ClientId=64a8236c-ce6a-4f5a-abd1-a83ec221c7e7&start=1&length=10000000&fromdate=01/01/2022&enddate=12/13/2022"
    response_sms = requests.get(url, params= data)
    return response_sms.data

