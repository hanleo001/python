import math
def isprime (x):
    from math import sqrt
    n=2
    m=False
    while n <= sqrt(x):
        if x%n==0 :
            m=m+True 
            break
        n+=1
    return m

def n_weishu_of_x (x,n):
    for i in range (n):

        y=x-math.floor(x/10)*10
        x=math.floor(x/10)
    return y


def weishu(x):
    n=0
    while x!= 0:
        x=math.floor(x/10)
        n=n+1
    return n
    
def weishufanghe(x):
    n=1
    s=0
    for i in range(weishu(x)):
        s=s+n_weishu_of_x(x,n)**2
        n=n+1
    return s 
