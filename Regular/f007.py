'''
In this bite we will look at this small server log finding the first and last system shutdown events:

INFO 2014-07-03T23:27:51 supybot Shutdown initiated.
...
INFO 2014-07-03T23:31:22 supybot Shutdown initiated.

You need to calculate the time between these two events. First extract the timestamps from the log entries and convert them to datetime objects. 
Then use datetime.timedelta to calculate the time difference between them.
You can assume the logs are sorted in ascending order. Check out the docstrings and the TESTS for more info.

Good luck and keep calm and code in Python!
'''


from datetime import datetime
import os
import urllib.request

SHUTDOWN_EVENT = 'Shutdown initiated'

# prep: read in the logfile
tmp = os.getenv("TMP", "/tmp")
logfile = os.path.join(tmp, 'log')
urllib.request.urlretrieve(
    'https://bites-data.s3.us-east-2.amazonaws.com/messages.log',
    logfile
)

with open(logfile) as f:
    loglines = f.readlines()


# for you to code:

def convert_to_datetime(line):
    """TODO 1:
       Extract timestamp from logline and convert it to a datetime object.
       For example calling the function with:
       INFO 2014-07-03T23:27:51 supybot Shutdown complete.
       returns:
       datetime(2014, 7, 3, 23, 27, 51)
    """
    # get index of the first letter that's a number
    first_num_index = 0
    for index, letter in enumerate(line):
        if letter.isnumeric():
            first_num_index = index
            break
    # extract just datetime sequence
    date_string = line[first_num_index:][0:19]

    # convert to datetime object using the log time format
    format = "%Y-%m-%dT%H:%M:%S"
    date = datetime.strptime(date_string, format)

    return date


def time_between_shutdowns(loglines):
    """TODO 2:
       Extract shutdown events ("Shutdown initiated") from loglines and
       calculate the timedelta between the first and last one.
       Return this datetime.timedelta object.
    """
    shutdown_times = [convert_to_datetime(line) for line in loglines if SHUTDOWN_EVENT in line]
    return shutdown_times[-1] - shutdown_times[0]

print(convert_to_datetime(loglines[5]))
print(time_between_shutdowns(loglines))
