import boto3

client = boto3.client('lambda')


def lambda_handler(event, context):
    try:
        print(event)

        path = event.get("path")
        params = path.split('/')
        lambda_name = params[0]

        params = {
            'FunctionName': lambda_name,
            'InvocationType': 'RequestResponse'
        }

        if event.get("httpMethod") != 'GET':
            params['Payload'] = event.get("body")

        response = client.invoke(**params)

        print(response['Payload'].read())
        return {
            "isBase64Encoded": False,
            "statusCode": 200,
            "body": response['Payload'].read()
        }
    except Exception as e:
        return {
            "isBase64Encoded": False,
            "statusCode": 500,
            "body": str(e)
        }
