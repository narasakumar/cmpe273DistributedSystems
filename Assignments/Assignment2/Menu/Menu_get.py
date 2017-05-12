from __future__ import print_function
import boto3

def lambda_handler(event, context):
    dynamodbTable = boto3.resource('dynamodb').Table('PizzaMenu')
    userinput_menu_id = event['params']['path']['menu-id']

    database_response = dynamodbTable.get_item(
        Key={
            'menu_id': userinput_menu_id,
        }
    )
    json_data = database_response['Item']
    return json_data
