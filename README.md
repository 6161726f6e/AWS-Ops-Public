## Searches cloudtrail logs.
**NOTE: AWS recently changed max log entries returned to 50.  So, narrowing timeframe will provide best results.**
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
                        UTC Time to start search for. Format = 2019-12-25-hh:mm
  -e ENDDATE, --enddate ENDDATE
                        UTC Time to end search for. Format = 2019-12-25-hh:mm

```
### Sample Search
```
$ python3 Search-CloudTrail-Logs.py  -p IAMUser -s 2021-01-23-19:57 -e 2021-01-23-19:59
setting pattern IAMUser
setting startdate 2021-01-23-19:57
setting enddate 2021-01-23-19:59
('{"eventVersion":"1.08","userIdentity":{"type":"IAMUser","principalId":"XXXX","arn":"arn:aws-us:iam::XXXXXXX:user/deployment_service_account","accountId":"XXXXXX","accessKeyId":"XXXXXX","userName":"XXXXXX"},"eventTime":"2021-01-23T19:59:00Z","eventSource":"ec2.amazonaws.com","eventName":"ModifyInstanceAttribute","awsRegion":"us-west-1","sourceIPAddress":"XXXXXX","userAgent":"aws-cli/1.11.173 '
 'Python/2.7.18 Linux/4.9.51-10.52.amzn1.x86_64 '
 'botocore/1.7.31","errorCode":"Client.UnauthorizedOperation","errorMessage":"You '
 'are not authorized to perform this operation. Encoded authorization failure '
 'message: '
 'XXXXX<REDACTED>...","requestParameters":{"instanceId":"XXXXXX","disableApiTermination":{"value":false}},"responseElements":null,"requestID":"afded655-0376-4a87-8ed5-e5424b92d862","eventID":"5c98ff54-7fbe-409c-9341-ad4e21c0941a","readOnly":false,"eventType":"AwsApiCall","managementEvent":true,"eventCategory":"Management","recipientAccountId":"XXXXXX"}')
----------------------------------------------------
('{"eventVersion":"1.08","userIdentity":{"type":"IAMUser","principalId":"XXXXX","arn":"arn:aws-us:iam::XXXX:user/XXXX","accountId":"XXXX","accessKeyId":"XXXXX","userName":"XXXXX"},"eventTime":"2021-01-23T19:58:59Z","eventSource":"autoscaling.amazonaws.com","eventName":"DescribeAutoScalingInstances","awsRegion":"us-west-1","sourceIPAddress":"XXXXXX","userAgent":"aws-cli/1.11.173 '
 'Python/2.7.18 Linux/4.9.51-10.52.amzn1.x86_64 '
 'botocore/1.7.31","requestParameters":null,"responseElements":null,"requestID":"8fc202d0-d6a8-43ae-b4b8-65a04cfe75c8","eventID":"bc2919d1-e73c-44a3-87bd-85acb8363248","readOnly":true,"eventType":"AwsApiCall","managementEvent":true,"eventCategory":"Management","recipientAccountId":"XXXXXX"}')
----------------------------------------------------

********************** SUMMARY **********************
PULLED 50 LOG ENTRIES
SEARCH FOR 'IAMUser' yielded 2 results
*****************************************************

```
