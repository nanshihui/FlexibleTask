#!/usr/bin/python
#coding:utf-8
from TaskTool import TaskTool

class example(TaskTool):

    def task(self,req,threadname):
        print req


if __name__=='__main__':
# 1 multithreading
# 0 multiprocess
# 2 greenlet
    t=example(runtype=1)
    t.add_work([1,2,3])