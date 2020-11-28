import json
import hashlib
import time

#
# Blockchain solver written in python - deployed as AWS lambda
#
def BcSolver(event, context):

    qs = event['queryStringParameters']
    q = qs['q']
    p = qs['p']
    b = qs['b']
    x = qs['x']
    m = qs['m']

    baseStr = b + q + p 
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
        "parentHash" : p,
        "blockId" : b,
        "query" : q,
        "executionTimeMs" : round(elapsedTime * 1000)
    }


    response = {
        "statusCode": 200,
        "body": json.dumps(solution)
    }

    return response

