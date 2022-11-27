def Ugly(n):
    while n%2==0:
        n/=2
    while n%3==0:
        n/=3
    while n%5==0:
        n/=5
    return True if n==1 else False
 






