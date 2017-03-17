# coding:utf-8
# author by @xiaoyusilen

import base_task

# definite the func you would like to run as a task project
def work():
    print "Hello the world~"

# the first key is your func_name,
# the second key is your first run time,
# the third to the sixth key is the cycle you want
# please change t
base_task.runTask(work, t="yyyy-mm-dd hh:mm:ss", day=0, hour=0, min=1, second=0)