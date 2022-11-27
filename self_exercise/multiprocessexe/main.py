from multiprocessing import Process
from random import randint
from time import time,sleep

def download(name):
    print("start:"+name)
    time_sleep=randint(1,4)
    sleep(time_sleep)
    print("end:"+name)

def main1():
    print("multiprocess")
    start=time()
    task1=Process(target=download,args=(str(1),))
    task1.start()
    task2=Process(target=download,args=("2",))
    task2.start()
    task1.join()
    task2.join()
    end=time()
    print(end-start)    

def main2():
    print("normal")
    start=time()
    download("1")
    download("2")
    end=time()
    print(end-start)

main1()
main2()