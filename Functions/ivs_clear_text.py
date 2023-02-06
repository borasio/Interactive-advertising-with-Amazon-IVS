import json
import boto3
import os


def lambda_handler(event, context):
    ivs = boto3.client("ivs")
    arn = os.environ['IVSARN']
    metadata = ivs.put_metadata(
          channelArn=arn,
          metadata='{\"type\": \"clear\"}'
        )
    # TODO implement
    return {
        'statusCode': 200,
        'body': json.dumps('Function Done')
    }
