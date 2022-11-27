from time import time


print("begin")
def is_prime(n):
    if n==2:
        return True
    elif n%2==0:
        return False
    for i in range(3,int(n**0.5+1),2):
        if n%i==0:
            return False
    return True
start_time=time()
p=0
for i in range(2,10**8):
    if is_prime(i):
        p+=1
end_time=time()
print("the amount of the prime number under 10**8 is {}".format(p))
print("Time used:{} ".format(end_time-start_time))

