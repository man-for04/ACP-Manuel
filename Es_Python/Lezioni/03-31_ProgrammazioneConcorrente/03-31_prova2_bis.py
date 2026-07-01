#daemon threads

from threading import *
import time

def thread_1():
    for i in range(5):
        print('this is 👹 thread T')
        time.sleep(2)

#creating a thread
T = Thread(target = thread_1, daemon = True)

#starting of thread T
T.start() #mi aspetto stampi 5 volte
time.sleep(5)
print("this is main Thread")
