

if __name__=="__main__":
    def Duplic(list1):
        a=set(list1)
        return True if len(a)<len(list1) else False
    print(Duplic([1,2,3,11]))