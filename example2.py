#!/usr/bin/python
#coding:utf-8
import lighttask
def example(self,data,taskname):
    print data
    return None
if __name__=='__main__':
    data=[1,2,3]
    lighttask.addwork(example,data,runtype=1, poolsize=2,doublepool=True)
## if you want to use  pool both  in gevent  and multiprocess ,just set doublepool=True