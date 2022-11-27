import threading
import time
def helloprint(a):
    print("hello {}".format(time.time()))
    
threadss=[]
for i in range(100):
    threadss.append(threading.Thread(helloprint,(1,))
    threadss[i].start()

for i in threadss:
    i.join()
