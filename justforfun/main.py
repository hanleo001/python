import register 

with open(".\item.txt","rt") as t:
    all_item=t.read().split()
    mark_for_setup=all_item[0]
if mark_for_setup!=0:
    mainpath="请输入安装目录："
    if mainpath[0]=="\"":
        mainpath=mainpath[1:-1]
    with open(".\item.txt","wt") as t:
        all_item[0]="1"
        t.write("".join(all_item))

x=input("欢迎回来，请输入用户名：")
x=input("按任意键结束")
