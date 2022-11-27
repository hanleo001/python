def Hanoi(n,i,j,k):
    if n==1:
        print(f"{i}->{k}")
    else:
        Hanoi(n-1,i,k,j)
        print(f'{i}->{k}')
        Hanoi(n-1,j,i,k,)
    return

def Hanoi_plus(n,i,j,k):
    if n==1:
        print(f"{i}->{j}")
        print(f"{j}->{k}")
    else:
        Hanoi_plus(n-1,i,j,k)
        print(f"{i}->{j}")
        Hanoi_plus(n-1,k,j,i)
        print(f"{j}->{k}")
        Hanoi_plus(n-1,i,j,k)

def circle(n):
    a=list(range(1,n+1))
    b=a.copy()
    p=1
    while len(b)>1:
        for k in a:
            if p%2==0:
                b.remove(k)
            p+=1
        a=b
        b=a.copy()
    return a[0]

def circle2(n):
    if n==1:
        return 1
    elif n%2==0:
        return 2*circle(n//2)-1
    else: return 2*circle((n-1)//2)+1

def circle3(n):
    m=0
    while 2**m<=n:
        m+=1
    m-=1
    l=n-2**m
    return 2*l+1


