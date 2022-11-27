from time import time


print("begin")
def Fibonacci(n):
    if n==0 or n==1:
        return True
    else:
        return Fibonacci(n-1)+Fibonacci(n-2)

start_time=time()
p=Fibonacci(40)
end_time=time()
print("the answer is {}".format(p))
print("Time used:{} ".format(end_time-start_time))

