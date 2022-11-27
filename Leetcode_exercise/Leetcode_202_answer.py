from tkinter import N


def isHappy (self,n):
    set1=set()
    while n not in set1 :
        set1.add(n)
        temp=0
        while n:
            n,val=divmod(n,10)
            temp+=val**2
        n=temp
    return True if n==1 else False