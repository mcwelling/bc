import boto3
from botocore.exceptions import ClientError

dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
table = dynamodb.Table('ballot')

def lambda_handler(event, context):
    try:
        table.delete_item(
            Key={
                'ballot': "ballot",
            }
        )

    except ClientError as e:
        return(e)
    except:
        return("Ballot oes not exist")
    return{
        'statusCode': 200,
        'headers': {
            'Access-Control-Allow-Headers': 'Content-Type',
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Methods': 'OPTIONS,POST,GET'
        },
        'body':"Success"
    }