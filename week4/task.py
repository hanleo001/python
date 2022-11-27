from functools import cache
import math
from time import time

def is_triangle(a,b,c):
    result=a+b>c and b+c>a and c+a>b
    return result

def delta(a,b,c):
    delta_=b*b-a*4*c
    if delta_==0:
        return 1
    return 2 if delta_>0 else 0

def is_prime(n):
    for i in range(2,int(n**0.5)+1):
        if n % i==0:
            return False
    return True

def is_leap(year):
    return True if year%400==0 or (year%100!=0 and year%4==0) else False

def f5(x):
    if x<-2:
        return x**4
    elif x<2:
        return math.sin(x)
    else: 
        return math.exp(x)

def f6(x):
    if x in [0,1]:
        return 1
    else:
        return f6(f6(x//2))+1

@cache
def f7_1(x):
    if x in [0,1]:
        return 1
    else:
        return f7_1(x-1)+f7_1(x-2)

@cache
def f7_2(x):
    if x in range(3):
        return 1
    else:
        return f7_2(x-1)+2*f7_2(x-2)-f7_2(x-3)

def f7_3(n):
    if n==0:
        return 2
    elif n==1:
        return 3
    else: return f7_3(n-2)*f7_3(n-1) 

@cache
def f7_4(m,n):
    if m*n==0:
        return 1
    else:
        return f7_4(m,n-1)+f7_4(m-1,n)-f7_4(m-1,n-1)    

def f7_1_(n):
    ai=1
    aij=1
    for i in range(1,n):
        aij,ai=ai+aij,aij
    return aij

def f7_2_(n):
    ai1=ai2=ai3=1
    for i in range(1,n):
        ai1,ai2,ai3=ai2,ai3,ai3+2*ai2-ai1
    return ai3

def f7_3_(n):
    ai0=2
    ai1=3
    for i in range(n-1):
        ai1,ai0=ai1*ai0,ai1
    return ai1

def f7_4_(m,n):
    rowi1=[i*0 for i in range(n)]
    for x in range(1,m):
         rowi0=rowi1
         rowi1[0]=0
         for y in range(1,n):
            rowi1[y]=rowi1[y-1]+rowi0[y]-rowi0[y-1]
    return rowi1[-1]

def middle(a,b,c):
    temp_list=[a,b,c]
    temp_list.sort()
    return temp_list[1]

def zeros(n):
    p=0
    while n%10==0:
        p+=1
    return p


def list22(p):
    if p==0:
        return [0]
    max2=int(math.log2(p))
    weishu2=max2+1
    result2=[0*i for i in range(weishu2)]
    while max2!=0:
        result2[max2]=1
        p-=2**max2
        if p==0:
            return result2
        elif p==1:
            result2[0]=1
            return result2
        max2=int(math.log2(p))

def Hamdist(a,b):  
    result1=0
    list1=list22(a)
    list2=list22(b)
    for i in range(min(len(list1),len(list2))):
        if list1[i]==list2[i]:
            result1+=1
    return result1

def Hanoi(n,x,y,z):
    if n ==1:
        print(f"{x}-->{z}")
    else:
        Hanoi(n-1,x,z,y)
        print(f"{x}-->{z}")
        Hanoi(n-1,y,x,z)


def is_valid(n):
    list1=[n]
    while n!=1:
        if n%2:
            n=3*n+1
        else:
            n=n/2
        if n in list1:
            return False
        list1.append(n)
    return True

def que3n(largestnum):
    result1=True
    for i in range(largestnum):
        k=i+1
        result1=result1 and is_valid(k)
    return result1






        

    



