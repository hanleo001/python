import math
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

def fanghe(x):
    n=1
    s=0
    for i in range(weishu(x)):
        s=s+n_weishu_of_x(x,n)**2
        n=n+1
    return s 

x=int(input('enter a positive integer number'))
set1=set()
sum2=1
while sum2 not in set1:
    set1.add(sum2)
    sum2=fanghe(x)
    x=sum2
    print (sum2)
if int(round(sum2))==int(1) :
    print("True ")
else: print("False")