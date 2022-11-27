class array:
    #先弄一维和二维的吧
    def __init__(self,lis):
        if not isinstance(lis,list):
            raise TypeError #暂不知应抛出什么异常
        self.__setndim(lis)
        self.shape=self.__getshape(lis)
        self.size=self.__getsize()
    def __setndim(self,lis):
        temp_type=type(lis[-1])
        for i in range(len(lis)-1):
            if type(lis[i])!=temp_type:
                raise TypeError
        if temp_type==type([1]):
            self.ndim=2
        else: self.ndim=1
    def __getshape(self,lis):
        if self.ndim==1:
            return (len(lis),)
        if self.ndim==2:
            row=len(lis)
            colome=len(lis[-1])
            for i in range(len(lis)-1):
                if len(lis[i])!=colome:
                    raise IndexError
        return (row,colome)
    def __getdtype(self,lis):
        pass
    def __getsize(self):
        if self.ndim==1:
            return self.shape[0]
        if self.ndim==2:
            return self.shape[0]*self.shape[1]
    def __getitemsize(self):
        pass
    


if __name__=="__main__":


    
        