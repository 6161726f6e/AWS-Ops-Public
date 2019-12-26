# Search-CloudTrail-Logs.py
# Author: Aaron Dhiman
# Summary: This script pulls logs matching a search query from CloudTrail Logs.
# Arguments:
#   searchPattern [OPTIONAL] - filter out logs, searching for specific string.
#   timeframe [OPTIONAL] - number of minutes to search for

import boto3
import sys
import re
import pprint
import argparse
from datetime import datetime, timedelta

# global variables
searchPattern = ''		# default: blank filter
timeframe = 600			# default: 10 minutes 

def getArgs():
    global searchPattern
    global timeframe
 
    helpText = 'This script pulls logs matching a search query from CloudTrail Logs.'
    # initiate the parser
    parser = argparse.ArgumentParser(description = helpText)
    parser.add_argument("-V", "--version", help="Show program version", action="store_true")
    parser.add_argument("-p", "--pattern", action='store', type=str, help="Pattern to search for.  Default is \'\'")
    parser.add_argument("-t", "--timeframe",  action='store', type=int, help="Timeframe to search for in minutes.  Default is 10")

    # read arguments from the command line
    args = parser.parse_args()

    # check for --version or -V
    if args.version:
        print("this is version 0.1")

    # store variables
    if args.pattern:
    	print("setting pattern "+str(args.pattern))
    	searchPattern = args.pattern

    if args.timeframe:
    	print("setting timeframe "+str(args.timeframe))
    	timeframe = args.timeframe

def pullLogs(searchPattern,timeframe):
    client = boto3.client('cloudtrail')
    responseDict = client.lookup_events(
        StartTime=datetime.utcnow() - timedelta(seconds=timeframe),
        EndTime=datetime.utcnow(),
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
    # Get Command Line variables or set defaults
#    try:
#        searchPattern = sys.argv[1]
#    except IndexError:
#    	print("Using Default filter \'\'")
		#searchPattern = ''
 #   try:
  #  	timeframe = int(sys.argv[2]) * 60
   # except IndexError:
    #	print("Using Default timeframe of 10 minutes")
 #       timeframe = 600     # default = 10 minutes
    getArgs()
    print("args = "+str(searchPattern)+" "+str(timeframe))
    pullLogs(searchPattern,timeframe)