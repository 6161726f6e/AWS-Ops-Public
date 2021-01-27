# Searches cloudtrail logs, pulling last 50 events by default.
## Options to filter by pattern and dates:

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

