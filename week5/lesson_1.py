import functools
import itertools
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
# for i in range(30,41):
#     a=time()
#     b=fibonacci(i)
#     c=time()
#     print(str(b)+"\n\n\n")
#     print(c-a)

def permutaion(n):
    if n ==1:
        return [(1,)]
    else:
        newlist=[]
        listall=permutaion(n-1)
        for item in listall:
            for k in range(n):
                nitem=item[:k]+(n,)+item[k:]
                newlist.append(nitem)
        return newlist

def valid(sla,n):
    for i in range(n):
        for j in range(i+1,n):
            if sla[i]-sla[j]==i-j or i+sla[i]==j+sla[j]:
                return False
    return True

# i=0
# for sla in itertools.permutations(list(range(9))):
#     if valid(sla,9):
#         i+=1

# print(i)


def sum(list1):
    p=0
    for i in list1:
        p+=i
    return p 

def factory(n):
    allnumber=[1,n]
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            allnumber.append(i)
            allnumber.append(int(n/i))
    allnumber.sort()
    return allnumber

def sumalllist(list1):
    p=0
    for item in list1:
        if isinstance(item,list):
            p+=sumalllist(item)
        elif isinstance(item,int) or isinstance(item,float):
            p+=item
        elif isinstance(item,str):
            pass
        elif isinstance(item,tuple):
            p+=sumalltuple(item)
        else: return "wrong"
    return p

def sumalltuple(tuple1):
    p=0
    for item in tuple1:
        if isinstance(item,list):
            p+=sumalllist(item)
        elif isinstance(item,int) or isinstance(item,float):
            p+=item
        elif isinstance(item,str):
            pass
        elif isinstance(item,tuple):
            p+=sumalltuple(item)
        else: return "wrong"
    return p

def sumDigits(n):
    n=str(n)
    p=0
    for i in range(len(n)):
        p+=int(n[i])
    return p









