import math
def nofx (x,n):
    for i in range (n):

        y=x-math.floor(x/10)*10
        x=math.floor(x/10)
    return y

x=int(input('x'))
n=int(input('n'))
print(nofx(x,n))