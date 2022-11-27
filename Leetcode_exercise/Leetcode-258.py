def Add_Digits(n):
    n=str(n)
    n=[int(n[i]) for i in range(len(n))]
    while len(n)>1:
        a=n.pop()
        b=n.pop()
        if a+b>=10:
            n.append((a+b)%10)
            n.append((a+b)//10)
        else:n.append(a+b)
    return n[0]

