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
