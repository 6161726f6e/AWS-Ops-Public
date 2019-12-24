# Search-CloudTrail-Logs.py
# Author: Aaron Dhiman
# Summary: This script pulls logs matching a search query from CloudTrail Logs.
# Arguments:
#   searchPattern [OPTIONAL] - filter out logs, searching for specific string
#   timeframe [OPTIONAL] - number of minutes to search for

import boto3
import sys
import re
import pprint
#from datetime import date
#import json
from datetime import datetime, timedelta

def pullLogs(searchPattern,timeframe):
    client = boto3.client('cloudtrail')
    responseDict = client.lookup_events(
        StartTime=datetime.utcnow() - timedelta(seconds=timeframe),
        EndTime=datetime.utcnow(),
        MaxResults=500,
    )
    #print(responseDict)
    #print('----------------------------------------------------')
    #for item in responseDict:
    #	print(item)

    eventsList = responseDict['Events']
    #print(events[0]['Username'])
    pp = pprint.PrettyPrinter(indent=4)
    i=0
    j=0
    while i < len(eventsList):
        p = re.compile('.*(%s).*'%searchPattern)
        m = p.search(eventsList[i]['CloudTrailEvent'])
        if m:
            #print(m)
            pp.pprint(eventsList[i]['CloudTrailEvent'])
            print('----------------------------------------------------')
            j=j+1
        i=i+1
    print('\n********************** SUMMARY **********************')
    print('PULLED ' + str(len(eventsList)) + ' LOG ENTRIES')
    print('SEARCH FOR \'' + searchPattern + '\' yielded ' + str(j) + ' results')
    print('*****************************************************')

if __name__ == "__main__":
    # Get Command Line variables or set defaults
    try:
        searchPattern = sys.argv[1]
    except IndexError:
        searchPattern = ''
    try:
        timeframe = int(sys.argv[2]) * 60
    except IndexError:
        timeframe = 600     # default = 10 minutespullLogs()

    pullLogs(searchPattern,timeframe)