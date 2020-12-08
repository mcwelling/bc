import boto3
import json

db_obj = boto3.resource('dynamodb')
queue_table = db_obj.Table('vote_queue')

def lambda_handler(event, context):

    qs = event['queryStringParameters']
    constant = "constant"
    voter_id = qs['voter_id']
    payload = qs['payload']
    
    queue_table.put_item(
    Item={
        'constant': constant,
        'voter_id': voter_id,
        'payload': payload
    })
    
    return {
        'statusCode': 200,
        'headers': {
                'Access-Control-Allow-Headers': 'Content-Type',
                'Access-Control-Allow-Origin': '*',
                'Access-Control-Allow-Methods': 'OPTIONS,POST,GET'
            },
        'body': json.dumps('Vote added to queue')
    }
