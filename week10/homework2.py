import time
def isprime1(x):
    if x in {2,3}:
        return True
    for i in range(2,x):
        if x%i==0:
            return False
    return True
            
def PN_1(n):
    time_start = time.time()
    number_pn = 0
    for i in range(2,n):
        if isprime1(i):
            number_pn+=1
    time_end = time.time()    
    return time_end - time_start, number_pn

def isprime2(x):
    if x==2:
        return True
    for i in range(2,int(x**0.5)+1):
        if x%i==0:
            return False
    return True

def PN_2(n):
    time_start = time.time()
    number_pn = 0
    for i in range(2,n):
        if isprime2(i):
            number_pn+=1
    time_end = time.time()    
    return time_end - time_start, number_pn

def isprime3(x):
    if x==2:
        return True
    for i in range(2,int(x**0.5)+1):
        if x%i==0:
            return False
    return True
def PN_3(n):
    time_start = time.time()
    number_pn = 0    
    if n<5 and n>=3:
        number_pn=2
    elif n==2:
        number_pn=1
    elif n==1:
        number_pn=0
    else:
        number_pn=2
        k=1
        while 6*k+1<=n:
            if isprime3(6*k+1):
                number_pn+=1
            k+=1
        k=1
        while 6*k-1<=n:
            if isprime3(6*k-1):
                number_pn+=1 
            k+=1
    time_end = time.time()    
    return time_end - time_start, number_pn

def PN_4(n):
    time_start = time.time()
    number_pn = 0
    numlist=list(range(2,n+1))
    for i in range(len(numlist)):
        if numlist[i]==-1:
            continue
        number_pn+=1
        step=numlist[i]
        place=i
        while place<=n-2:
            numlist[place]=-1
            place+=step
    time_end = time.time()    
    return time_end - time_start, number_pn

def pre_5(ev):
    s=0
    while ev&1==0:
        ev>>=1
        s+=1
    return s,ev

def prepass5(x,a):
    if a>=x:
        return True
    s,d=pre_5(x-1)
    q=pow(a,d,x)
    if q==1:
        return True
    for r in range(s):
        if q==x-1:
            return True
        q=pow(q,2,x)
    return False

def isprime5(x):
    if x==2:
        return True
    if x%2==0:
        return False
    else:
        lis_a=[2, 3]
        for a in lis_a:
            if not prepass5(x,a):
                return False
        return True

def PN_5(n):
    time_start = time.time()
    number_pn = 0
    for i in range(2,n+1):
        if isprime5(i):
            number_pn+=1
    time_end = time.time()
    return time_end - time_start, number_pn



# print(PN_1(1000000))
print(PN_2(10000000))
print(PN_3(10000000))
print(PN_4(10000000))
print(PN_5(10000000))

# start=time.time()
# print(isprime5(1000000000000037))
# end=time.time()
# print(end-start)
# , 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97