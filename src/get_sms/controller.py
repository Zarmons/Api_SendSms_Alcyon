import requests
import json

from datetime import date


def get_sms_sent(fromdate, enddate):
    args = {
        'ApiKey': 'Rq1vExJtdTs/oZuUzHm0vYQNGO3ifyoNke53wxlxUr4=',
        'ClientId': '64a8236c-ce6a-4f5a-abd1-a83ec221c7e7',
        'start': 1,
        'length': 10000000,
        'fromdate':  fromdate,
        'enddate':  enddate,
    }
        # apiKey: dl+FQ3GR1APhItJFV3YribLFH222STRBhM2KjrSauAU=
        # clientId: 03cd7ed3-a294-4daa-9350-76f92e99c7e6
        # date.today().strftime("%m/%d/%y")
    url = "https://api.reddantu.com/api/v2/GetSMS"
    response_sms = requests.get(url, params=args)
    response =  json.loads(response_sms._content)
    return response

