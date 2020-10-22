import json


def hello(event, context):

    # data = json.loads(event['body'])

    # number1 = data['number1']
    # number2 = data['number2']
    number1 = 20
    number2 = 10
    sum = number1 + number2
    difference = number1 - number2
    product = number1 * number2
    try:
        quotient = number1 / number2
    except ZeroDivisionError:
        quotient = 0

    # quotient = number1 / number

    response_body = {
        "Number1": number1,
        "Number2": number2,
        "Sum": sum,
        "Difference": difference,
        "Product": product,
        "Quotient": quotient,
    }

    response = {
        "statusCode": 200,
        "body": json.dumps(response_body)
    }

    return response

    # body = {
    #     "message": "Hello! Successfully Deploy",
    #     "input": event
    # }
    #
    # response = {
    #     "statusCode": 200,
    #     "body": json.dumps(body)
    # }
    #
    # return response

    # Use this code if you don't use the http event with the LAMBDA-PROXY
    # integration
