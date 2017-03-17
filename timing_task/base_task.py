# coding:utf-8
# author by @xiaoyusilen

import time
from datetime import datetime, timedelta

def runTask(func, t, day=0, hour=0, min=0, second=0):
    # Get current time and format
    strnow = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    # Print the current time
    print "Current time is: ", strnow

    # First run time and turn to time struct
    period = timedelta(days=day, hours=hour, minutes=min, seconds=second)
    strnext_time = time.strptime(t,'%Y-%m-%d %H:%M:%S')
    strnext_time = time.strftime('%Y-%m-%d %H:%M:%S', strnext_time)

    # First run time
    print "First run time is: ", strnext_time

    count = 0
    # wait for the first run time
    while True:

        # Get system current time
        now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        if str(now) == str(strnext_time):
            # calculate the run times
            count = count + 1
            # Get every start work time
            print "Start work: %s" % now
            # Call task func
            func()
            # maybe you should add try...catch... If the func carry out failed, you can get the status.
            print "You have run %d times. And this time is done." % count
            # Get next run time
            strnext_time = datetime.now() + period
            strnext_time = strnext_time.strftime('%Y-%m-%d %H:%M:%S')
            print "Next run time is: ", strnext_time
            # Continue
            continue