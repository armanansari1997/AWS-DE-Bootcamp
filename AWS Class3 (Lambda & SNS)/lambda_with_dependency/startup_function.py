import json
import requests

def custom_lambda(event, context):
    print(f"Event Data -> {event}")
    response = requests.get('https://www.google.com')
    print(response.text)
    
    return response.text