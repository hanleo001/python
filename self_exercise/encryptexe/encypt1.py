from cryptography.fernet import Fernet
def write_key(path):
    p=Fernet.generate_key()
    with open(path,"wb") as t:
        t.write(p)

def load_key(path):
    with open(path,"rb") as t:
        return t.read()

def getmessage(path):
    with open(path,"rt") as t :
        return t.read().encode() 
path=r"D:\BaiduSyncdisk\大学生活\计算导论\self_exercise\key1.key"
# write_key(path)
key=load_key(path)
f=Fernet(key)
# message1=getmessage(r"D:\BaiduSyncdisk\大学生活\计算导论\self_exercise\os_exe1.py")
# q=f.encrypt(message1)
# with open ("D:\BaiduSyncdisk\大学生活\计算导论\self_exercise\os_exe1_encrypted.py","wb") as y:
#     y.write(q)
with open(r"D:\BaiduSyncdisk\大学生活\计算导论\self_exercise\os_exe1_encrypted.py","rb") as messagetemp:
    message1=messagetemp.read()
new=f.decrypt(message1)
with open(r"D:\BaiduSyncdisk\大学生活\计算导论\self_exercise\ww00001.py","wb") as txt:
    txt.write(new)