import json

def lambda_handler(event, context):
    """
    A simple Lambda function that responds with a JSON message.
    """
    return {
        "statusCode": 200,
        "headers": {
            "Content-Type": "application/json"
        },
        "body": json.dumps({"message": "Hello, World!"})
    }
