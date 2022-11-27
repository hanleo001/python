def WordPatten(pattern,str1):
    target=str1.split()
    pattern=[i for i in pattern]
    dic=dict(zip(pattern,target))
    newstr=''
    for i in pattern:
        newstr=newstr+dic[i]+' '
    if str1+' '==newstr:
        return True
    else:return False

print(WordPatten("abba","dog cat cat dog"))