from __future__ import print_function
import boto3

def lambda_handler(event, context):
    dynamodbTable = boto3.resource('dynamodb').Table('PizzaMenu')
    userinput_menu_id = event['params']['path']['menu-id']
    database_response = dynamodbTable.delete_item(
        Key={
            'menu_id': userinput_menu_id,
        }
    )
    return "200 OK"
