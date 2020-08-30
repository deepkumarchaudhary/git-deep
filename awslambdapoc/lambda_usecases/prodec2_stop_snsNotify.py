import boto3
import Json
client = boto3.client('sns')
def lambda_handler(event, context):
    instance_id = event['details']['instance-id']
    message = "Hi Team - Instance with instance-id={}, has stopped".format(instance_id)
    client.publish(TopicArn='arn:aws:sns:us-west-2:915530126681:lambda-demo', Message=message)
