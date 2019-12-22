import boto3
import sys
import json
import time
from datetime import date

client = boto3.client('cloudtrail')
response = client.lookup_events(
#    LookupAttributes=[
#        {
#            'AttributeKey': 'EventName',
#            'AttributeValue': 'CreateAccessKey'
#        },
#    ],
#    StartTime=date.today(),
#    EndTime=date.today(),
    MaxResults=50,
)
print(response)
