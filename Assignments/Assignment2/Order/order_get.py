from __future__ import print_function
import boto3

def lambda_handler(event, context):
    dynamodbTable = boto3.resource('dynamodb').Table('Order')
    order_id = event['params']['path']['order_id']

    database_response = dynamodbTable.get_item(
        Key={
            'order_id': order_id,
        }
    )
    json_data = database_response['Item']
    return json_data
