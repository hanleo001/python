
class Triangle:
    def __init__(self, a=0, b=0, c=0):
        self.a, self.b, self.c = a, b, c

    def is_valid(self):
        return self.a>0 and self.b>0 and self.c>0 and self.a+self.b>self.c and self.b+self.c>self.a and self.c+self.a>self.b

    def set_edges(self, a, b,  c):
        self.a, self.b, self.c = a, b, c    

    def area(self):
        q = (self.a+self.b+self.c)/2
        return (q*(q-self.a)*(q-self.b)*(q-self.c)) ** 0.5

    def print(self): 
        print("my_geometry.Triangle: {}, {}, {}".format(self.a,self.b, self.c))
    
    def print_area(self):
        print("my_geometry.Area: {:.3f}".format(self.area())) # area()会报错, 必须加self 

    def __len__(self):
        return self.a+self.b+self.c
    
    def __str__(self):
        return "my_geometry:"+", ".join((str(self.a), str(self.b), str(self.c)))
    
    def __lt__(self, other):   # x<y                   lt: large than
        return self.a<other.a and self.b<other.b and self.c<other.c
    
    def __le__(self, other):  # x<=y                 less equal  
        return self.a<=other.a and self.b<=other.b and self.c<=other.c
    
    def __eq__(self, other): # x==y                 equal  
        return self.a==other.a and self.b<=other.b and self.c<=other.c

    def __ne__(self, other): # x!=y                   not equal
        return self.a!=other.a or self.b!=other.b or self.c!=other.c

    def __gt__(self, other):  # x>y                   greater than
        return self.a>other.a and self.b>other.b and self.c>other.c

    def __ge__(self, other): # x>=y                 greater equal
        return self.a>=other.a and self.b>=other.b and self.c>=other.c
