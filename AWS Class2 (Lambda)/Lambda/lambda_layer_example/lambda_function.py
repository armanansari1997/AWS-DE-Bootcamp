import json
from math_ops import *
from str_function import *

def lambda_handler(event, context):
    
    print(f"Event Data -> {event}")
    print("Trigger Received !!!")
    
    print(f"Square of a number : {square(8)}")
    print(f"Sum of two numbers : {sum(2, 4)}")
    print(f"Double the string : {double_str('Arman')}")
    
    # TODO implement
    return {
        'statusCode': 200,
        'body': json.dumps('Bye Bye')
    }