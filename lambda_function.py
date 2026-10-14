import json

def lambda_handler(event, context):
    name = event.get("name", "әлем")
    return {
        "statusCode": 200,
        "body": json.dumps({"message": f"Сәлем, {name}!"}, ensure_ascii=False)
    }
