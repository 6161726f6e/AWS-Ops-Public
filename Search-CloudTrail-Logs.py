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

# global variables
searchPattern = ''		# default: blank filter
startDate = datetime.combine(date.today(), time())
endDate = datetime.now()

def getArgs():
    global searchPattern, startDate, endDate
    
    helpText = 'This script pulls logs matching a search query from CloudTrail Logs.'
    # initiate the parser
    parser = argparse.ArgumentParser(description = helpText)
    parser.add_argument("-V", "--version", help="Show program version", action="store_true")
    parser.add_argument("-p", "--pattern", action='store', type=str, help="Pattern to search for.  Default is \'\'")
    parser.add_argument("-s", "--startdate",  action='store', type=str, help="UTC Time to start search for. Format = 2019-12-25-hh:mm")
    parser.add_argument("-e", "--enddate",  action='store', type=str, help="UTC Time to end search for. Format = 2019-12-25-hh:mm")

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

    if args.startdate:
    	print("setting startdate "+str(args.startdate))
    	startDate = args.startdate

    if args.enddate:
    	print("setting enddate "+str(args.enddate))
    	endDate = args.enddate

def pullLogs(searchPattern):
    client = boto3.client('cloudtrail')
    responseDict = client.lookup_events(
        StartTime=startDate,
        EndTime=endDate,
        MaxResults=1000,
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
    getArgs()
    pullLogs(searchPattern)
