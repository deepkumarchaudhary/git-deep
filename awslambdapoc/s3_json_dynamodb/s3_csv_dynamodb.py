import json
import boto3
s3_client = boto3.client('s3')
#dynamodb = boto3.client('dynamodb')
dynamodb = boto3.resource('dynamodb')

def lambda_handler(event, context):
    bucket = event['Records'][0]['s3']['bucket']['name']
    csv_file_name = event['Records'][0]['s3']['object']['key']
    #print (bucket)
    #print (csv_file_name)
    resp = s3_client.get_object(Bucket=bucket,Key=csv_file_name)
    #print (resp)
    data = resp['Body'].read().decode("utf-8")
    #print(data)
    table = dynamodb.Table('employees')
    employees = data.split("\n")
    for emp in employees:
        print (emp)
        emp_data = emp.split(",")
        try:
            table.put_item(
                Item = {
                    "emp_id" : emp_data[0],
                    "name" : emp_data[1],
                    "location" : emp_data[2]
                }
                )
        except Exception as e:
            print ("End Of File")
            # TODO implement
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
