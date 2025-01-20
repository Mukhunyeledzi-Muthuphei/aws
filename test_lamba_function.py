import json
from lambda_function import lambda_handler  # Assuming the function is in lambda_function.py

def test_lambda_handler():
    # Sample event and context (mocked for the test)
    event = {}  # Empty event for simplicity
    context = {}  # Empty context for simplicity (or you can mock this as needed)

    # Call the lambda_handler function with the mock event and context
    response = lambda_handler(event, context)
    
    # Verify the statusCode
    assert response["statusCode"] == 200
    
    # Verify the Content-Type header
    assert response["headers"]["Content-Type"] == "application/json"
    
    # Verify the body contains the expected message
    body = json.loads(response["body"])
    assert body["message"] == "Hello, World!"
