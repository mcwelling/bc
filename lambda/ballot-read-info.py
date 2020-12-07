import json
import boto3

db_obj = boto3.resource('dynamodb')
db_table = db_obj.Table('ballot')

def lambda_handler(event, context):
    
    response = db_table.get_item(
            Key={
                'ballot': "ballot"
            }
        )
    
    # TODO implement
    return {
        'statusCode': 200,
        'headers': {
            'Access-Control-Allow-Headers': 'Content-Type',
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Methods': 'OPTIONS,POST,GET'
        },
        'body': json.dumps(response)
    }
