def MoveZeroes(target):
    newtarget=[0 for i in target]
    p=0
    for i in target:
        if i!=0:
            newtarget[p]=i
            p+=1
    return newtarget

print(MoveZeroes([0,1,0,3,12])) 