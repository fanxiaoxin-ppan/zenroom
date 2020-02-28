# -*- coding: utf-8 -*-
import threading
import time

def run(taskName) :
    print u"任务 : {0}" .format(taskName)
    time.sleep(2)
    print u"{0} 任务执行完毕" .format(taskName) # 查看每个子线程

if __name__ == '__main__' :
    start_time = time.time()
    for i in range(3):
        thr = threading.Thread(target=run, args=(u"task-{0}" .format(i),))
        # 把子线程设置为守护线程
        thr.setDaemon(True)
        thr.start()
        # 查看主线程和当前活动的所有线程数
    print u"{0}线程结束，当线程数量 = {1}" .format(threading.current_thread().getName(), threading.active_count())
    print u"消耗时间 : {0}" .format(time.time() - start_time)