from __future__ import print_function
import boto3
from datetime import datetime

def lambda_handler(event, context):
    # TODO implement
    dynamodbTable_order = boto3.resource('dynamodb').Table('Order')
    dynamodbTable_menu = boto3.resource('dynamodb').Table('PizzaMenu')
    order_id = event['params']['path']['order_id']
    
    user_input = event['body-json']['input']
    
    database_response = dynamodbTable_order.get_item(
        Key={
            'order_id': order_id,
        }
    )
    
    order_data = database_response['Item']
    menu_id=order_data['menu_id']
    
    menu_details = dynamodbTable_menu.get_item(
        Key={
            'menu_id': menu_id,
        }
    )
    menu_data=menu_details['Item']
    
    if order_data['order1']['selection']=="-" :
        # "no selection"
        allselection=menu_data['selection']
        selection=allselection[int(user_input)-1]
        result = dynamodbTable_order.update_item(
        Key={
            'order_id': order_id,
        },
        UpdateExpression="SET order1.selection = :i",
        ExpressionAttributeValues={
            ':i': selection,
        },
        ReturnValues="UPDATED_NEW"
        )

        data = {}
        message="Which size do you want? "
        i = 1
        for item in menu_data['size'] :
            message = message + str(i)
            message = message + ". " + item + ", "
            i=i+1
            # message+=item+", "
        message=message[:-2]
        data['Message'] = message
        return data

    elif order_data['order1']['size']=="-" :
        # "no selection"
        allsize=menu_data['size']
        size=allsize[int(user_input)-1]
        cost=menu_data['price'][int(user_input)-1]
        time=datetime.now().strftime("%m-%d-%y %H:%M")
        result = dynamodbTable_order.update_item(
        Key={
            'order_id': order_id,
        },
        UpdateExpression="SET order_status = :s, order1.size = :i, order1.costs = :c, order1.order_time = :t",
        ExpressionAttributeValues={
            ':s': "processing",
            ':i': size,
            ':c': cost,
            ':t': time
        },
        ReturnValues="UPDATED_NEW"
        )
        
        data = {}
        message="Your order costs "+ cost +". We will email you when the order is ready. Thank you!"
        data['Message'] = message
        return data

