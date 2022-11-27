def some(arr):
    import math
    arr.sort()
    leng=len(arr)
    p=math.floor(leng*0.05)
    for i in range (p):
        arr.pop()
        arr.reverse()
        arr.pop()
    s=0
    f=len(arr)
    for i in range (len (arr)):
        s=s+arr.pop()
    return s/f

arr = [6,0,7,0,7,5,7,8,3,4,0,7,8,1,6,8,1,1,2,4,8,1,9,5,4,3,8,5,10,8,6,6,1,0,6,10,8,2,3,4]




