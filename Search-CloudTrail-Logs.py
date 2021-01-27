# Search-CloudTrail-Logs.py
# Author: Aaron Dhiman
# Summary: This script pulls logs matching a search query from CloudTrail Logs.
# Arguments:
#   searchPattern [OPTIONAL] - filter out logs, searching for specific string.
#   startDate [OPTIONAL] - UTC Time to start search for. Format = 2019-12-25-hh:mm.
#      Default = Beginning of current day.
#   endDate [OPTIONAL] - UTC Time to end search for. Format = 2019-12-25-hh:mm
#      Default = Current Time.

import boto3
import sys
import re
import pprint
import argparse
from datetime import datetime, date, time

def getArgs():
    helpText = 'This script pulls logs matching a search query from CloudTrail Logs.'
    # initiate the parser
    parser = argparse.ArgumentParser(description = helpText)
    parser.add_argument("-V", "--version", help="Show program version", action="store_true")
    parser.add_argument("-p", "--pattern", action='store', type=str, help="Pattern to search for.  Default is \'\'")
    parser.add_argument("-s", "--startDate",  action='store', type=str, help="UTC Time to start search for. Format = 2019-12-25-hh:mm")
    parser.add_argument("-e", "--endDate",  action='store', type=str, help="UTC Time to end search for. Format = 2019-12-25-hh:mm")

    # read arguments from the command line
    args = parser.parse_args()

    # check for --version or -V
    if args.version:
        print("\nPull-Cloud-Trail Version 0.1\n")
        sys.exit()

    # store variables
    if args.pattern:
    	print("setting pattern "+str(args.pattern))
    	searchPattern = args.pattern
    else:
        searchPattern = ''      # default: blank filter

    if args.startDate:
    	print("setting startDate "+str(args.startDate))
    	startDate = args.startDate
    else:
        startDate = datetime.combine(date.today(), time())

    if args.endDate:
    	print("setting endDate "+str(args.endDate))
    	endDate = args.endDate
    else:
        endDate = datetime.now()

    return(searchPattern,startDate,endDate)

def pullLogs(searchPattern,startDate,endDate):
    client = boto3.client('cloudtrail')
    responseDict = client.lookup_events(
        StartTime=startDate,
        EndTime=endDate,
        MaxResults=50,  #max AWS allows is 50
    )
    #print(responseDict)
    #print('----------------------------------------------------')
    #for item in responseDict:
    #	print(item)

    eventsList = responseDict['Events']
    #print(events[0]['Username'])
    pp = pprint.PrettyPrinter(indent=4)
    i=0	# count total
    j=0 # count matches
    p = re.compile('.*(%s).*' % searchPattern)
    while i < len(eventsList):
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
    searchPattern,startDate,endDate=getArgs()
    pullLogs(searchPattern,startDate,endDate)
