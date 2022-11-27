import itertools
import string
from random import randint
from random import uniform
import math
import re 


def pro1(target:list)->list:
    target=list(set(target))
    target.sort(reverse=True)
    return target
a=pro1([3,2,1,4,2,3,5])
print(a)

def pro2(s:str)->str:
    s=list(s)
    s.reverse()
    return ''.join(s)
print(pro2('hello world'))

def pro2_2(s:str)->str:
    s=list(s)
    s=s[::-1]
    return ''.join(s)
print(pro2_2("hello world"))

def pro3(n:int)->int:
    if n==0:
        return 0
    if n>0:
        p=[]
        while n>=10:
            p.append(n%10)
            n//=10
        p.append(n)
        p=p[::-1]
        n=0
        k=0
        for i in p:
            n+=i*(10**k)
            k+=1         
        return n
    if n<0:
        return -pro3(-n)
for i in [123,-123,120]:
    print(pro3(i))

def pro4():
    originlist=input("请输入两个列表(用空格分割元素),两个列表之间用分号分割： ").split(";")
    a=[int(i) for i in originlist[0].split()]
    b=[int(i) for i in originlist[1].split()]
    a,b=set(a),set(b)
    if a^b:
        return a&b
    else:
        print("no intersection")
        return False
print(pro4())

def pro5():
    strin='1'
    res=[]
    while strin!='0':
        strin=input("请输入句子(输入0并按回车结束):")
        strin_new=str.upper(strin)
        res.append(strin_new+'\n')
    res.pop()
    for i in res:
        print(i,end='')
    return ''.join(res)
pro5()        

def pro6():
    x=input("请输入个句子，我来倒着输出一下：")
    x=x[::-1]
    print(x)
pro6()




def pro8(s):
    return s[::-1]

def pro9(a,b):
    res=a+b
    res.sort()
    return res

def pro10():
    n=int(input("请输入最大数"))
    answer=randint(1,n)
    x=-1
    while x!=answer:
        x=int(input(f"请猜一个介于1到{n}的数(输入0结束游戏)："))
        if x==0:
            print(f"答案是{answer},欢迎再来玩。")
            return
        elif x>answer:
            print("Too large")
        elif x<answer:
            print("Too small")
    print(f"Right! The answer is {answer}.Bye!")
    return
pro10()

def pro10plus():
    n=float(input("请输入最大数"))
    answer=uniform(1,n)
    x=-1
    while x!=answer:
        x=float(input(f"请猜一个介于1到{n}的数(输入0结束游戏)："))
        if x==0:
            print(f"答案是{answer},欢迎再来玩。")
            return
        elif x>answer:
            print("Too large")
        elif x<answer:
            print("Too small")
    print(f"Right! The answer is {answer}.Bye!")
    return
pro10plus()

def pro11(n):
    for i in range(1,n*2):
        if i <=n:
            print('*'*i)
        else: 
            print('*'*(-i+2*n))
    return
pro11(5)

# ques1
def pro12(target:list)->list:
    odd=[]
    even=[]
    for i in target:
        if i%2==0:
            even.append(i)
        else:
            odd.append(i)
    return even,odd

def pro13(n):
    for i in range(1,n+1):
        for i in range(1,i+1):
            print(i,end=' ')
        print('')
pro13(5)

def pro14(n):
    for i in range(n):
        temp=[k for k in range(1,n-i+1)][::-1]
        for k in temp:
            print(k,end=" ")
        print("")
    return
pro14(5)

def pro15(n):
    pass

def pro16(n):
    return int(math.log10(n)+1)

def pro17(n):
    s=0
    for i in range(n):
        s+=int('2'*(i+1))
    return s
print(pro17(3))

def pro18():
    x=input("请设置一个密码：")
    a='abcdefghigklmnopqrstuvwmxyz'
    b=a.upper()
    c='1234567890'
    d={'$','#','@'}
    if len(x)<6 or len(x)>16:
        return False
    p=[0,0,0]
    for i in x:
        if i in a or i in b:
            p[0]+=1
        elif i in c:
            p[1]+=1
        elif i in d:
            p[2]+=1
    for i in p:
        if i<1:
            return False
    return True
print(pro18())

def pro18_():
    x=input("请设置一个密码：")
    p1=re.compile("[a-zA-Z]")
    p2=re.compile("\d")
    p3=re.compile("[$#@]")
    a,b,c=p1.search(x),p2.search(x),p3.search(x)
    if len(x)>=6 and len(x)<=16 and a.group(0) and b.group(0) and c.group(0) :
        return True
    else :
        return False
print(pro18_())

def pro19():
    p=[400]
    for j in range(0,9,2):
        for k in range(0,9,2):
            a=int(f'2{j}{k}')
            p.append(a)
    return p
print(pro19())

def pro20(k:str):
    vowel='aeiou'
    if k in vowel:
        print("vowel")
    else:
        print("consonant")
    return
pro20('s')

def pro21(n:int):
    d31={1,3,5,7,8,10,12}
    d30={4,6,9,11}
    if n==2:
        return 28
    if n in d31:
        return 31
    if n in d30:
        return 30
print(pro21(8))

def pro22(s:str):
    try:
        x=int(s)
        return True
    except:
        return False
# print(pro22("s"))
# print(pro22("52"))

def pro23():
    pass

def pro24(m,d):
    pass

def pro25():
    pass

def pro26():
    pass

def pro27():
    x=input("Input a year:")
    y=input("Input a month[1-12]:")
    z=input("Input a day[1-31]:")
    print(f"The next date is [yyyy-mm-dd] {x}-{y}-{z}")
pro27()

def pro28():
    for i in range(1,11):
        for j in range(1,11):
            print(f"{i:2}X{j:2}={i*j:3}",end=" ")
        print('')
    return
pro28()

n=4
a=itertools.permutations([i for i in range(1,n+1)])
print(list(a))

def Haino(i,j,k,n):
    if n==1:
        print(f"{i}->{k}")
    else:
        Haino(i,k,j,n-1)
        print(f'{i}->{k}')
        Haino(j,i,k,n-1)
    return
for i in range(1,6):
    print(f"Haino({i}):")
    Haino(1,2,3,i)
