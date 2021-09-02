import json
import boto3

db_obj = boto3.resource('dynamodb')
db_table = db_obj.Table('registration')

def lambda_handler(event, context):
    
    qs = event['queryStringParameters']
    id = qs['voter_id']
    
    response = db_table.get_item(
            Key={
                'voter_id': id
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
