import json
import boto3

db_obj = boto3.resource('dynamodb')
table = db_obj.Table('vote_chain')
reg_table = db_obj.Table('registration')

def lambda_handler(event, context):
    scan = table.scan()
    with table.batch_writer() as batch:
        for each in scan['Items']:
            batch.delete_item(
                Key={
                    'voter_id': each['voter_id'],
                    'timestamp': each['timestamp']
                }
            )
    
    table.put_item(
        Item={
            'voter_id': 'root',
            'timestamp': 0,
            'ballot': 'root',
            'block_hash': 'root',
            'constant': 'constant'
        }
    )
    
    scan = reg_table.scan()
    with table.batch_writer() as batch:
        for each in scan['Items']:
            reg_table.update_item(
                Key={
                    'voter_id': each['voter_id'],
                },
                UpdateExpression="set voted_yn = :r",
                ExpressionAttributeValues={
                    ':r': 'N',
                }
            )
    
    return {
        'statusCode': 200,
        'headers': {
            'Access-Control-Allow-Headers': 'Content-Type',
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Methods': 'OPTIONS,POST,GET'
        },
        'body': json.dumps('Table deleted')
    }
