def FindMissnum(target):
    for i in range(1+len(target)):
        if not i in target:
            return i

