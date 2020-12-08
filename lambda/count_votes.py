import json
import boto3
from boto3.dynamodb.conditions import Key

db_obj = boto3.resource('dynamodb')
table = db_obj.Table('vote_chain')

def lambda_handler(event, context):
    vote_count = []
    scan = table.scan()
    
    for item in scan['Items']:
        if(item['ballot'] != "root"):
            for ballot in json.loads(item['ballot']):
                proposal_id = int(ballot['id'])-1
                if(len(vote_count) <= proposal_id):
                    vote_count.append({})
                    for option in ballot['options']:
                        vote_count[proposal_id][option] = 0
                selection = ballot['selected']
                vote_count[proposal_id][selection] += 1

    
    return {
        'statusCode': 200,
        'headers': {
            'Access-Control-Allow-Headers': 'Content-Type',
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Methods': 'OPTIONS,POST,GET'
        },
        'body': json.dumps(vote_count)
    }
