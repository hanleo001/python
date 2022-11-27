class Triangle:
    def __init__(self,a,b,c):
        self.a,self.b,self.c=a,b,c
    def is_valid(self):
        return self.a+self.b>self.c and self.a+self.c>self.b and self.c+self.b>self.a
    def area(self):
        p=(self.a+self.b+self.c)*0.5
        return (p*(p-self.a)*(p-self.b)*(p-self.c))**0.5
    def set_edges(self,a,b,c):
        self.a,self.b,self.c=a,b,c
    def print(self):
        print(f"The Triangle:{self.a},{self.b},{self.c}")

class Vector:
    def __init__(self,*args):
        self.elements=args
    def __getitem__(self,index):
        return self.elements[index]
    def __str__(self) -> str:
        return "["+",".join(self.elements)+"]"
    def __lt__(self,vector):
        if len(self.elements)<len(vector.elements):
            return True
        else:return False
    def __le__(self,vector):
        if len(self.elements)<=len(vector.elements):
            return True
        else:
            return False
    def __gt__(self,vector):
        if len(self.elements)>len(vector.elements):
            return True
        else:return False   
    def __ge__(self,vector):
        if len(self.elements)>=len(vector.elements):
            return True
        else:return False
    def __eq__(self,vector):
        if len(self.elements)==len(vector.elements):
            return True
        else:return False
    def __ne__(self,vector):
        if len(self.elements)!=len(vector.elements):
            return True
        else:return False
    def __setitem__(self,index,element):
        self.elements[index]=element
    def length(self):
        p=0
        for i in self.elements:
            p+=i**2
        return p**0.5
    def print_length(self):
        print("The length of the vector is {}".format(self.length()))
    def angle(self):
        return [i/self.length() for i in self.elements]
    def print_angle(self):
        print(f"The angle of the vector is {self.angle()}")
    def dot(self,other):
        p=0
        for i,item in enumerate(self.elements):
            p+=item*other.elements[i]
        return p
    def scale(self,ratio):
        self.elements=[i*ratio for i in self.elements]
    def is_orthogonal(self,other):
        return True if self.dot(other)==0 else False

a=Vector(1,2,3,4,5,6)
b=Vector(1,-1/2,1/3,-1/4,1/5,-1/6)
print(a.is_orthogonal(b))
print(a.angle())
print(a.elements)
a.scale(5)
print(a.elements)
print(a[2])
a[2]=8
print(a[2])
print(a.elements)
print(b.elements)
print(a>b,a>=b,a<b,a<=b,a==b,a!=b)