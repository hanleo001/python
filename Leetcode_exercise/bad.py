import os
x=input("请输入命令：")
while x!='0':
    if x=='make':
        y=int(input("number:"))
        for i in range(y):
            if not os.path.exists("D:"+f"\{i}mumu{(i**2+1+i*9)**(0.1)}"):
                os.makedirs("D:"+f"\{i}mumu{(i**2+1+i*9)**(0.1)}")
        print('succeed!')
        x=input("请输入命令：")
    if x=='remove':
        y=int(input("number:"))
        for i in range(y):
            pathx="D:"+f"\{i}mumu{(i**2+1+i*9)**(0.1)}"
            if os.path.exists(pathx):
                os.rmdir(pathx)
        print("complete")
        x=input("请输入命令：")
    else:
        print("密码错误，程序结束")
        break
else:print("end")
input()