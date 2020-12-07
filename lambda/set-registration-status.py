import json
import boto3
from boto3.dynamodb.conditions import Key

db_obj = boto3.resource('dynamodb')

# registered voter table
reg_table = db_obj.Table('registration')

def lambda_handler(event, context):
    
    qs = event['queryStringParameters']
    voter_id = qs['voter_id']
    
    registration_status = reg_table.update_item(
            Key={
                'voter_id': voter_id,
            },
            UpdateExpression="set voted_yn = :r",
            ExpressionAttributeValues={
                ':r': 'P',
            }
        )
    
    return {
        'statusCode': 200,
        'headers': {
            'Access-Control-Allow-Headers': 'Content-Type',
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Methods': 'OPTIONS,POST,GET'
        },
        'body': json.dumps(registration_status)
    }
