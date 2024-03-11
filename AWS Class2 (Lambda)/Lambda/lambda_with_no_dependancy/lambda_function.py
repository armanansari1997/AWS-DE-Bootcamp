import json

def get_square(num):
    return num ** 2

def lambda_handler(event, context):
    
    print(f"Event Data : -> {event}")
    print("Trigger Received !!!")
    
    num = 5
    res_square = get_square(num)
    
    print(f"Square of {num} is {res_square}")
    
    # Todo implement
    return {
        'statusCode': 200,
        'body': json.dumps({'Square': res_square})
    }