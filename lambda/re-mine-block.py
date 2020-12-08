import json
import json
import hashlib
import time
import datetime

def lambda_handler(event, context):
    
    qs = event['queryStringParameters']
    ballot = qs['ballot']           # completed ballot
    parent_hash = qs['parent_hash'] # parent block hash
    voter_id = qs['voter_id']       # ID of the current block
    x = "0000"                      # Complexity (e.g. 0000)
    m = 1000000                     # Max attempts (e.g. 10E6)
    
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
    
    elapsedTime = time.time() - start
    
    solution = {
        "nonce" : hashSolution['nonce'],
        "blockHash" : hashSolution['blockHash'],
        "found" : hashSolution['found'],
        "parent_hash" : parent_hash,
        "voter_id" : voter_id,
        "ballot" : ballot,

    }
    
    return {
        'statusCode': 200,
        'headers': {
            'Access-Control-Allow-Headers': 'Content-Type',
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Methods': 'OPTIONS,POST,GET'
        },
        'body': json.dumps(solution)
    }
