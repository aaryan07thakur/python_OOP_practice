# https://www.geeksforgeeks.org/dunder-magic-methods-python/ : here we can find all the magic 
#m3thod and we can create our own data types


class Fraction:
    def __init__(self,n,d) -> None:
        self.num=n
        self.den=d

    def __str__(self) -> str:
        return "{}/{}".format(self.num, self.den)
    
    def __add__(self,other):
        temp_num=self.num*other.den +other.num*self.den
        temp_den=self.den*other.den
        return "{}/{}".format(temp_num, temp_den)
    

    def __sub__(self,other):
        temp_num=self.num*other.den -other.num*self.den
        temp_den=self.den*other.den
        return "{}/{}".format(temp_num, temp_den)
    

    def __mul__(self,other):
        temp_num=self.num*other.num
        temp_den=self.den*other.den
        return "{}/{}".format(temp_num, temp_den)
    

    def __truediv__(self,other):
        temp_num=self.num*other.den
        temp_den=self.den*other.num
        return "{}/{}".format(temp_num, temp_den)
    


x=Fraction(3,4)
y=Fraction(5,6)
# print(type(x))
print(x)
print(y)
print(x+y)
print(x-y)
print(x*y)