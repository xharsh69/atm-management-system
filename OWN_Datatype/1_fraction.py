class Fraction:

    def __init__(self,n:int,d:int):
        self.n= n
        self.d=d

    def __str__(self):
        return "{}/{}".format(self.n,self.d)
    
    def __add__(self, other):
        tum_n= self.n*other.d+self.d*other.n
        tum_d = self.d*other.d 
        return "{}/{}".format(tum_n,tum_d)
    

    def __sub__(self, other):
        tum_n= self.n*other.d-self.d*other.n
        tum_d = self.d*other.d 
        return "{}/{}".format(tum_n,tum_d)
    
    def __mul__(self, other):
        
        return "{}/{}".format(self.n*other.n,self.d*other.d)
    
    def __truediv__(self, other):
        
        temp_n= self.n*other.d
        temp_d= self.d*other.n
        return "{}/{}".format(temp_n,temp_d)
    

    
    
        


x=Fraction(5,8)

y = Fraction(3,5)


print(x+y)
print(x-y)
print(x*y)
print(x/y)