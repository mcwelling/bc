import boto3
from botocore.exceptions import ClientError

dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
table = dynamodb.Table('ballot')

def lambda_handler(event, context):
    try:
        table.put_item(
            Item={
                'ballot': "ballot",
                'info': event['queryStringParameters']
            },
            ConditionExpression='attribute_not_exists(ballot)'
        )

    except ClientError as e:
        if e.response['Error']['Code'] == 'ConditionalCheckFailedException':
            return("Ballot already exists")
        else:
            return("Unexpected error: %s" % e)
    return{
        'statusCode': 200,
        'headers': {
            'Access-Control-Allow-Headers': 'Content-Type',
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Methods': 'OPTIONS,POST,GET'
        },
        'body':"Success"}