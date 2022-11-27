import functools
from re import I
from time import time
@functools.cache
def factorial(n):
    print("{} begins".format(n))
    if n==0 or n==1:
        return 1
    else :
        f=factorial(n-1)
        print("{} done".format(n-1))
        return f*n

def factorial1(n):
    print("{} begins".format(n))
    if n==0 or n==1:
        return 1
    else :
        f=factorial1(n-1)
        print("{} done".format(n-1))
        return f*n

def gcd(a,b):
    if a>b:
        a,b=b,a
    if b%a==0:
        return a
    else:
        return gcd(b%a,a)

@functools.cache
def fibonacci(n):
    if n==0 or n==1:
        return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2)


def fibonacci(n):
    memory={0:1,1:1}
    if n not in memory:
        memory[n]=fibonacci(n-1)+fibonacci(n-2)
    return memory[n]

def Hanoi(n,x,y,z):
    if n ==1:
        print(f"{x}-->{z}")
    else:
        Hanoi(n-1,x,z,y)
        print(f"{x}-->{z}")
        Hanoi(n-1,y,x,z)
for i in range(30,41):
    a=time()
    b=fibonacci(i)
    c=time()
    print(str(b)+"\n\n\n")
    print(c-a)









