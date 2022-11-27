from genericpath import isfile
import os 
path1="D:\\"

def makemanydirs(path_,n=1):
    for i in range(1,n+1):
        pathnew=path_+"\\"+"{}".format(i)
        if os.path.isdir(pathnew):
            continue
        os.makedirs(pathnew)


def makehellotxt(path_):
    newfile=open(path_+"\\"+"hello.txt","wt")
    newfile.write("Hello. Have a good day!")
    newfile.close()
    allitem=os.listdir(path_)
    for i in allitem:
        if os.path.isdir(path_+"\\"+i):
            makehellotxt(path_+"\\"+i)

def removethisfile(path_,*name):
    for namedetail in name:
        if os.path.isfile(path_+"\\"+namedetail):
            os.remove(path_+"\\"+namedetail)
        allitem=os.listdir(path_)
        for i in allitem:
            if os.path.isdir(path_+"\\"+i):
                removethisfile(path_+"\\"+i,namedetail)
            
for i in range(1000):
    os.rmdir("E:\\223\\{}".format(i))

removethisfile("E:\\223","hello.txt")
makemanydirs(r"E:\223",1000)
os.mkdir("E:\\223")

makemanydirs("E:\\223",100)
os.rename("E:\\223\\52","E:\\223\\0")

