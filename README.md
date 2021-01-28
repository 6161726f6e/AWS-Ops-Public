## Searches cloudtrail logs.
**NOTE: AWS recently changed max log entries returned to 50.  So, narrowing timeframe will provide best results.**
**NOTE: Searches are case-INsensitive**
### Options to filter by pattern and dates:

```
$ python3 Search-CloudTrail-Logs.py --help
usage: Search-CloudTrail-Logs.py [-h] [-V] [-p PATTERN] [-s STARTDATE] [-e ENDDATE]

This script pulls logs matching a search query from CloudTrail Logs.

optional arguments:
  -h, --help            show this help message and exit
  -V, --version         Show program version
  -p PATTERN, --pattern PATTERN
                        Pattern to search for. Default is ''
  -s STARTDATE, --startdate STARTDATE
                        UTC Time to start search for. Format = '2019-12-25 hh:mm'
  -e ENDDATE, --enddate ENDDATE
                        UTC Time to end search for. Format = '2019-12-25 hh:mm'

```
### Sample Search
```
╰─⠠⠵ python3 Search-CloudTrail-Logs.py -p list -s '2021-01-28 11:33' -e '2021-01-28 11:35'
setting pattern list
setting startDate 2021-01-28 11:33
setting endDate 2021-01-28 11:35
{
  "eventVersion": "1.08",
  "userIdentity": {
    "type": "AssumedRole",
    "principalId": "XXXXXXX",
    "arn": "arn:aws-us:sts::XXXXX:assumed-role/XXXXXX/XXXXXXX",
    "accountId": "XXXXX",
    "accessKeyId": "XXXXXX",
    "sessionContext": {
      "sessionIssuer": {
        "type": "Role",
        "principalId": "XXXXXX",
        "arn": "arn:aws-us:iam::XXXXX:role/XXXXXX",
        "accountId": "XXXXX",
        "userName": "XXXXXX"
      },
      "webIdFederationData": {},
      "attributes": {
        "mfaAuthenticated": "false",
        "creationDate": "2021-01-28T06:09:30Z"
      },
      "ec2RoleDelivery": "2.0"
    }
  },
  "eventTime": "2021-01-28T11:35:00Z",
  "eventSource": "ssm.amazonaws.com",
  "eventName": "ListInstanceAssociations",
  "awsRegion": "us-west-1",
  "sourceIPAddress": "XXXX",
  "userAgent": "aws-sdk-go/1.25.41 (go1.13.15; linux; amd64) amazon-ssm-agent/",
  "requestParameters": {
    "instanceId": "XXXXXXX",
    "maxResults": 20
  },
  "responseElements": null,
  "requestID": "XXXXXX",
  "eventID": "XXXXXX",
  "readOnly": true,
  "resources": [
    {
      "accountId": "XXXXX",
      "ARN": "arn:aws-us:ec2:us-west-1:XXXXX:instance/XXXXXXX"
    }
  ],
  "eventType": "AwsApiCall",
  "managementEvent": true,
  "eventCategory": "Management",
  "recipientAccountId": "XXXXX"
}
----------------------------------------------------
{
  "eventVersion": "1.08",
  "userIdentity": {
    "type": "AssumedRole",
    "principalId": "XXXXXX",
    "arn": "arn:aws-us:sts::XXXXX:assumed-role/XXXXXX/XXXXXXX",
    "accountId": "XXXXX",
    "accessKeyId": "XXXXXX",
    "sessionContext": {
      "sessionIssuer": {
        "type": "Role",
        "principalId": "XXXXXX",
        "arn": "arn:aws-us:iam::XXXXX:role/XXXXXX",
        "accountId": "XXXXX",
        "userName": "XXXXXX"
      },
      "webIdFederationData": {},
      "attributes": {
        "mfaAuthenticated": "false",
        "creationDate": "2021-01-28T07:18:04Z"
      },
      "ec2RoleDelivery": "2.0"
    }
  },
  "eventTime": "2021-01-28T11:34:34Z",
  "eventSource": "ssm.amazonaws.com",
  "eventName": "ListInstanceAssociations",
  "awsRegion": "us-west-1",
  "sourceIPAddress": "XXXX",
  "userAgent": "aws-sdk-go/1.25.41 (go1.12.11; windows; amd64) amazon-ssm-agent/",
  "requestParameters": {
    "instanceId": "XXXXXXX",
    "maxResults": 20
  },
  "responseElements": null,
  "requestID": "XXXXXX",
  "eventID": "XXXXX",
  "readOnly": true,
  "resources": [
    {
      "accountId": "XXXXX",
      "ARN": "arn:aws-us:ec2:us-west-1:XXXXX:instance/XXXXXXX"
    }
  ],
  "eventType": "AwsApiCall",
  "managementEvent": true,
  "eventCategory": "Management",
  "recipientAccountId": "XXXXX"
}
----------------------------------------------------
{
  "eventVersion": "1.08",
  "userIdentity": {
    "type": "AssumedRole",
    "principalId": "XXXXXX",
    "arn": "arn:aws-us:sts::XXXXX:assumed-role/XXXXXXX/XXXXXXX",
    "accountId": "XXXXX",
    "accessKeyId": "XXXXXXXXXXXXXXXXXX",
    "sessionContext": {
      "sessionIssuer": {
        "type": "Role",
        "principalId": "XXXXXXXXXXXXXXXX",
        "arn": "arn:aws-us:iam::XXXXX:role/XXXXXXXX",
        "accountId": "XXXXX",
        "userName": "XXXXXXXXX"
      },
      "webIdFederationData": {},
      "attributes": {
        "mfaAuthenticated": "false",
        "creationDate": "2021-01-28T09:02:49Z"
      },
      "ec2RoleDelivery": "2.0"
    }
  },
  "eventTime": "2021-01-28T11:33:00Z",
  "eventSource": "ssm.amazonaws.com",
  "eventName": "ListInstanceAssociations",
  "awsRegion": "us-west-1",
  "sourceIPAddress": "XXXXXXX",
  "userAgent": "aws-sdk-go/1.25.41 (go1.13.15; linux; amd64) amazon-ssm-agent/",
  "requestParameters": {
    "instanceId": "XXXXXXXXX",
    "maxResults": 20
  },
  "responseElements": null,
  "requestID": "XXXXXXX",
  "eventID": "XXXXXXXXX",
  "readOnly": true,
  "resources": [
    {
      "accountId": "XXXXX",
      "ARN": "arn:aws-us:ec2:us-west-1:XXXXX:instance/XXXXX"
    }
  ],
  "eventType": "AwsApiCall",
  "managementEvent": true,
  "eventCategory": "Management",
  "recipientAccountId": "XXXXX"
}
----------------------------------------------------

********************** SUMMARY **********************
PULLED 36 LOG ENTRIES
SEARCH FOR 'list' yielded 3 results
*****************************************************
```
