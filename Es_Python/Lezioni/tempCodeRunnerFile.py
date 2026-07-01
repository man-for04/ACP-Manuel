#Non daemon-threads

from threading import *
import time

def thread_1():
    for i in range(5):
        print('this is non-daemon thread')
        time.sleep(2)

#creazione thread
T=Thread(target = thread_1)

#starting of thread T
T.start()

#main thread stop execution till 5 sec
time.sleep(5)
print('main Thread execution')