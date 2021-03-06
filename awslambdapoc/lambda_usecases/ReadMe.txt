Introduction:
1) No servers needs to manage - Serverless
2) Autoscale Automatically
3) Lambda runs on latest generation of computers, processors
4) We do not pay for lambda if code is idle - Function can create and leave it idle
5) Minimum Memory - 128 MB and accordingly CPU allocated
6) Automatically allocate memory to 3 GB and CPU accordingly for processing

Use Case: Lambda is for background work only, if something needs to manage in background
1) Upload Json/CSV in S3 and insert data in Dynamodb
2) Create Thumbnail of images uploaded in S3
3) Resize Image in S3 post uploaded
4) Transcoding Videos Automatically when uploaded in S3
5) Automation of EBS snapshot in timely manner and store in S3
6) AWS Sample Example: Real-time file processing
7) AWS Sample Example: Web applications handling
8) When EC2 stop, send out a notification at email id



Scenario 1: Json upload on S3 to Dynamodb - Code file - s3_json_dynamodb.json
1) Created bucket in S3 named - javahome-json-test
2) Create policy s3_json_dynamodb.json
3) create role s3_json_dynamodb and attached inline policy and aws managed policy of s3 full access
4) Create trigger from S3 with all the events
  S3: javahome-json-test
5) upload file in bucket and it will trigger the event
6) and put the records in dynamo db

Scenario 2: CSV upload on S3 to Dynamodb - Code file - s3_csv_dynamodb.json
1) Similar to Above:
2) Upload csv on S3 and event trigger with .csv and any type of trigger
3) loop around the data present in csv and enter data in s3_json_dynamodb

Scenario 3: AWS Sample Example: Real-time file processing - Code - lambda-refarch-fileprocessing

#You can use Amazon S3 to trigger AWS Lambda to process data immediately after an upload. You can also connect to an existing Amazon EFS file system directly, which enables massively parallel shared access for large scale file processing. For example, you can use Lambda to thumbnail images, transcode videos, index files, process logs, validate content, and aggregate and filter data in real-time.

Scenario 4: AWS Sample Example: Real-time file processing - Code - lambda-refarch-webapp

#By combining AWS Lambda with other AWS services, developers can build powerful web applications that automatically scale up and down and run in a highly available configuration across multiple data centers – with zero administrative effort required for scalability, back-ups or multi-data center redundancy.
