from __future__ import print_function
import boto3
import json

def lambda_handler(event, context):
    # TODO implement
    dynamodbTable_order = boto3.resource('dynamodb').Table('Order')
    dynamodbTable_menu = boto3.resource('dynamodb').Table('PizzaMenu')
    request_body = event['body-json']
    menu_id = request_body['menu_id']
    
    # "order_status": "processing"
    # "order": {
    #     "selection": "Cheese",
    #     "size": "Large",
    #     "costs": "15.00",
    #     "order_time": "mm-dd-yyyy@hh:mm:ss"
    # }
    # extra_data = {}
    request_body['order_status']="New"
    
    order_details1 = {}
    order_details1['selection'] = "-"
    order_details1['size'] = "-"
    order_details1['costs'] = "-"
    order_details1['order_time'] = "-"
    request_body['order1']=order_details1
    
    dynamodbTable_order.put_item(Item=request_body)
    
    database_response = dynamodbTable_menu.get_item(
        Key={
            'menu_id': menu_id,
        }
    )
    menu_data = database_response['Item']
    
    
    data = {}
    message="Hi " + request_body['customer_name'] + ", please choose one of these selection:  "
    i = 1
    for item in menu_data['selection'] :
        message = message + str(i)
        message = message + ". " + item + ", "
        i=i+1
        # message+=item+", "
    message=message[:-2]
    data['Message'] = message
    return data
