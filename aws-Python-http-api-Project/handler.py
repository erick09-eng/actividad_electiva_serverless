import json


def nombre_E(event, context):
    body = {
        "message": "Erick Sbeastian Bolivar Arboleda",
        "input": event,
    }

    response = {"statusCode": 200, "body": json.dumps(body)}

    return response
def codigo_E(event, context):
    body = {
        "message": "240220232006",
        "input": event,
    }

    response = {"statusCode": 200, "body": json.dumps(body)}

    return response
def correo_E(event, context):
    body = {
        "message": "erick.bolivar.2257@eam.edu.co",
        "input": event,
    }

    response = {"statusCode": 200, "body": json.dumps(body)}

    return response
