import json
import boto3
import secrets
import time
import datetime

# Lambda with Gateway trigger and DynamoDB Destination
# Take in data from form and process it to be put into database tables

def lambda_handler(event, context):
    # build custom id
    secretsGenerator = secrets.SystemRandom()
    # returns current date and time
    x = str(time.time()) + "-"
    x += str(secretsGenerator.randint(0, 9999999999))
    client_dynamo=boto3.resource('dynamodb')
    # table name
    table=client_dynamo.Table('Touchless-CU')
    # try to send data
    dictA = json.loads(event['body'])
    # dictA = json.loads(json.dumps(event))
    
    # parse custom json
    dictB = {}
    dictB['data_id'] = str(x)
    dictC = {}
    dictC['date'] = str(datetime.datetime.utcnow())
    dictA.update(dictB)
    dictA.update(dictC)

    # merged_json = json.dumps(dictA)

    # try and put in table
    try:
        response=table.put_item(Item=dictA)
        return ("Done")
    except:
        # raise exception (remeber to send primary key)
        raise
