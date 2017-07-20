#!/usr/bin/python
#coding:utf-8
import time
def addwork(job=None,data=None,runtype=1,poolsize=10,doublepool=False):
    if doublepool:
        import TaskTool
        TaskTool.add_work(func=job,data=data,runtype=runtype, poolsize=poolsize)

    else:

        if runtype==0:
            from multiprocessing import Pool
        elif runtype==1:
            from multiprocessing.dummy import Pool
        else:
            from gevent.pool import Pool
            from gevent import monkey
            monkey.patch_all(thread=False)
        jobpool = Pool(poolsize)
        # for i in data:
        #     jobpool.apply(job,i)
        jobpool.map(job,data)
        if runtype==1 or runtype==2:
            jobpool.close()
        jobpool.join()
def test(data):

    print data



testdata=[(1,),(2,)]
if __name__=='__main__':
    addwork(test,testdata,runtype=0)
    time.sleep(1)
    addwork(test,testdata,runtype=1)

