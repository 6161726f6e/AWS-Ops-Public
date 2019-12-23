import boto3
import sys
import re
import pprint
#from datetime import date
#import json
#import time

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
    MaxResults=20,
)
#print(responseDict)
#print('----------------------------------------------------')
#for item in responseDict:
#	print(item)

searchPattern = sys.argv[1]

eventsList = responseDict['Events']
#print(events[0]['Username'])
pp = pprint.PrettyPrinter(indent=4)
i=0
while i < len(eventsList):
    p = re.compile('.*(%s).*'%searchPattern)
    m = p.search(eventsList[i]['CloudTrailEvent'])
    if m:
        #print(m)
        pp.pprint(eventsList[i]['CloudTrailEvent'])
        print('----------------------------------------------------')
    i=i+1

