from __future__ import print_function
import boto3
import json

def lambda_handler(event, context):
    dynamodbTable = boto3.resource('dynamodb').Table('PizzaMenu')
    userinput_menu_id = event['params']['path']['menu-id']
    request_body = event['body-json']

    result = dynamodbTable.update_item(
        Key={
            'menu_id': userinput_menu_id,
        },
        UpdateExpression="SET selection = :i",
        ExpressionAttributeValues={
            ':i': request_body['selection'],
        },
        ReturnValues="UPDATED_NEW"
    )

    if result['ResponseMetadata']['HTTPStatusCode'] == 200 and 'Attributes' in result:
        # data = {}
        # data['menu_id'] = userinput_menu_id
        # data['selection']=result['Attributes']['selection']
        # return data
        return "200 OK"
        # return result['Attributes']['selection']
