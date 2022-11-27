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

s=0
p=2
n=float(input('enter a non-negative number')) 
if n <= 2:
    print(0)
else:
    while p<n:
        if isprime(p):
            pass
        else:s+=1
        p+=1
    print(s)

         
    

