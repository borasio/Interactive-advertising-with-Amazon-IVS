import json
import boto3
import os

def lambda_handler(event, context):
    dynamodb = boto3.resource("dynamodb", region_name="eu-west-1")
    table = dynamodb.Table(os.environ['DynamoDb_Table'])
    step = boto3.client("stepfunctions")

    responseupdate = table.update_item(
                       Key={
                            'Id': "1"
                       },
                       UpdateExpression="SET #ttlexpired=:newValue, #stepalreadydone=:newAlready, #productlive=:newOnline",
                       ExpressionAttributeNames={
                            '#ttlexpired': 'ttlexpired',
                            '#stepalreadydone': 'stepalreadydone',
                            '#productlive': 'productlive'
                       },
                       ExpressionAttributeValues={
                            ':newValue': "0",
                            ':newAlready': "0",
                            ':newOnline': "0"
                       },
                       ReturnValues="UPDATED_NEW"
                    )
    return {
        'statusCode': 200,
        'body': json.dumps('Processed')
    }
