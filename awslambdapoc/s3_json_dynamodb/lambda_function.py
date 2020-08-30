import json
import boto3
s3_client = boto3.client('s3')
#dynamodb = boto3.client('dynamodb')
dynamodb = boto3.resource('dynamodb')
def lambda_handler(event, context):
    #print (str(event))
    bucket = event['Records'][0]['s3']['bucket']['name']
    json_file_name = event['Records'][0]['s3']['object']['key']
    print (bucket)
    print (json_file_name)
    json_object = s3_client.get_object(Bucket=bucket,Key=json_file_name)
    print (json_object)
    jsonFileReader = json_object['Body'].read()
    jsonDict = json.loads(jsonFileReader)
    table = dynamodb.Table('employees')
    #table = dynamodb.Table('test')
    table.put_item(Item=jsonDict)
    # TODO implement
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
