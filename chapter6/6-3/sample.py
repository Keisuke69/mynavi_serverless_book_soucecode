import boto3
import json

print('Loading function')
dynamo = boto3.client('dynamodb')

operations = {
    'DELETE': lambda dynamo, x: dynamo.delete_item(**x),
    'GET': lambda dynamo, x: dynamo.scan(**x),
    'POST': lambda dynamo, x: dynamo.put_item(**x),
    'PUT': lambda dynamo, x: dynamo.update_item(**x),
}

print(operations)