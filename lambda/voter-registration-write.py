import json
import boto3
from botocore.exceptions import ClientError
import hashlib

db_obj = boto3.resource('dynamodb')
db_table = db_obj.Table('registration')

def lambda_handler(event, context):
    
    qs = event['queryStringParameters']
    first = qs['first']
    last = qs['last']
    street = qs['street']
    city = qs['city']
    state = qs['state']
    zip = qs['zip']
    dob = qs['dob']
    email = qs['email']
    voted_yn = 'N'
    
    hashStr = first + last + street + city + state + zip + dob + email
    voter_id = hashlib.sha256(hashStr.encode()).hexdigest()
    
    try:
        db_table.put_item(
        Item={
            'voter_id': voter_id,
            'voter_fname': first,
            'voter_lname': last,
            'street': street,
            'city': city,
            'state': state,
            'zip': zip,
            'voter_dob': dob,
            'email': email,
            'voted_yn': voted_yn
        },
        ConditionExpression='attribute_not_exists(voter_id)'
    )
    except ClientError as e:
        if e.response['Error']['Code'] == 'EntityAlreadyExists':
            print("User already exists")
        else:
            print("Unexpected error: %s" % e)

    
    
    return {
        'statusCode': 200,
        'headers': {
            'Access-Control-Allow-Headers': 'Content-Type',
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Methods': 'OPTIONS,POST,GET'
        },
        'body': json.dumps(voter_id)
    }
