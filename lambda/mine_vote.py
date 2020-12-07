import json
import boto3
from boto3.dynamodb.conditions import Key
import hashlib
import time
import datetime

#
# Augmented Blockchain solver written in python - citation: p
#

db_obj = boto3.resource('dynamodb')

# block chain
chain_table = db_obj.Table('vote_chain')

# registered voter table
reg_table = db_obj.Table('registration')

#queue table
queue_table = db_obj.Table('vote_queue')

def lambda_handler(event, context):
    constant = "constant"
    
    #get ballot from queue
    queue_resp = queue_table.query(KeyConditionExpression=Key('constant').eq(constant))
    if(len(queue_resp['Items']) == 0):
        response = {
            "statusCode": 200,
            'headers': {
                'Access-Control-Allow-Headers': 'Content-Type',
                'Access-Control-Allow-Origin': '*',
                'Access-Control-Allow-Methods': 'OPTIONS,POST,GET'
            },
            "body": json.dumps("Queue is empty")
        }
        return(response)
    voter_id = queue_resp['Items'][0]['voter_id']
    ballot = queue_resp['Items'][0]['payload']
    
    #delete ballot from queue
    queue_table.delete_item(Key={'constant': constant, 'voter_id': voter_id})
    
    #set some constants
    x = "0000"                      # Complexity (e.g. 0000)
    m = 1000000                     # Max attempts (e.g. 10E6)
    
    #get parent hash
    gsi = "constant-timestamp-index"
    response = chain_table.query(
            IndexName=gsi,
            KeyConditionExpression=Key("constant").eq(constant), 
            ScanIndexForward=False, 
            Limit=1
        )
    parent_hash = response['Items'][0]['block_hash']

    #generate hash
    baseStr = ballot + parent_hash + voter_id
    hashSolution = {}

    start = time.time()

    for i in range(int(m)):
        hashStr = baseStr + str(i)
        if hashlib.sha256(hashStr.encode()).hexdigest().startswith(x):
            hashSolution = {
                "nonce": i,
                "blockHash" : hashlib.sha256(hashStr.encode()).hexdigest(),
                "found" : True
            }
            break
    else:
        hashSolution = {
                "nonce": i,
                "blockHash" : "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF",
                "found" : False
            }
        response = {
            "statusCode": 200,
            'headers': {
                'Access-Control-Allow-Headers': 'Content-Type',
                'Access-Control-Allow-Origin': '*',
                'Access-Control-Allow-Methods': 'OPTIONS,POST,GET'
            },
            "body": json.dumps("Error - hash failure, block not committed.")
        }
        return response

    elapsedTime = time.time() - start
    commitTime = int(datetime.datetime.utcnow().timestamp())

    solution = {
        "nonce" : hashSolution['nonce'],
        "blockHash" : hashSolution['blockHash'],
        "found" : hashSolution['found'],
        "parent_hash" : parent_hash,
        "voter_id" : voter_id,
        "ballot" : ballot,
        "timestamp" : commitTime,
        "constant": constant
    }
    
    #add to blockchain table
    try:
        chain_table.put_item(
            Item={
                "block_hash" : hashSolution['blockHash'],
                "parent_hash" : parent_hash,
                "voter_id" : voter_id,
                "nonce" : hashSolution['nonce'],
                "ballot" : ballot,
                "timestamp" : commitTime,
                "constant": constant
            }
        )
        response = {
            "statusCode": 200,
            'headers': {
                'Access-Control-Allow-Headers': 'Content-Type',
                'Access-Control-Allow-Origin': '*',
                'Access-Control-Allow-Methods': 'OPTIONS,POST,GET'
            },
            "body": json.dumps(solution)
        }
        
        registration_status = reg_table.update_item(
            Key={
                'voter_id': voter_id,
            },
            UpdateExpression="set voted_yn = :r",
            ExpressionAttributeValues={
                ':r': 'Y',
            }
        )
        
    except ClientError as e:
        message = "Unexpected error: " + str(e)

        response = {
            "statusCode": 200,
            'headers': {
                'Access-Control-Allow-Headers': 'Content-Type',
                'Access-Control-Allow-Origin': '*',
                'Access-Control-Allow-Methods': 'OPTIONS,POST,GET'
            },
            "body": json.dumps(message)
        }

    return response