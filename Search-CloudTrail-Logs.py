import boto3
import sys
#import json
#import time
import pprint
#from datetime import date

client = boto3.client('cloudtrail')
responseDict = client.lookup_events(
#    LookupAttributes=[
#        {
#            'AttributeKey': 'EventName',
#            'AttributeValue': 'CreateAccessKey'
#        },
#    ],
#    StartTime=date.today(),
#    EndTime=date.today(),
    MaxResults=2,
)
print(responseDict)
print('----------------------------------------------------')
#for item in responseDict:
#	print(item)

eventsList = responseDict['Events']
#print(events[0]['Username'])
pp = pprint.PrettyPrinter(indent=4)
pp.pprint(eventsList[0])
print('----------------------------------------------------')
pp.pprint(eventsList[1])

