import json
import boto3
from boto3.dynamodb.conditions import Key
from decimal import Decimal

class DecimalEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Decimal):
            return float(obj)
        return json.JSONEncoder.default(self, obj)

db_obj = boto3.resource('dynamodb')
table = db_obj.Table('vote_chain')

def lambda_handler(event, context):
    gsi = "constant-timestamp-index"
    scan = table.query(
        IndexName=gsi,
        KeyConditionExpression=Key("constant").eq("constant"), 
        ScanIndexForward=True, 
    )
    
    item_list = []
    
    for item in scan['Items']:
        item_list.append(item)

    
    return {
        'statusCode': 200,
        'headers': {
            'Access-Control-Allow-Headers': 'Content-Type',
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Methods': 'OPTIONS,POST,GET'
        },
        'body': json.dumps(item_list,cls=DecimalEncoder)
    }
