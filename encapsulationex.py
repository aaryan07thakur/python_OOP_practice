# class Bankaccount:
#     def __init__(self, balance) -> None:
#         self._balance=balance   # private 

#     def deposit(self, amount):
#         self._balance+=amount

#     def withdraw(self, amount):
#         self._balance-=amount

#     def get_balance(self):
#         return self._balance

# abc=Bankaccount(1000)   # creating object and storing on abc
# # abc.deposit(600000)
# # abc.withdraw(100000)
# # print(f"the final balance is : {abc.get_balance}")








#Public Members

# class public:
#     def __init__(self) -> None:
#         self.name="dipesh Thakur"   #public attribute
#     """ Public Attribute (name): This attribute is declared without any underscore prefixes. 
#                                 It is accessible from anywhere, both inside and outside of the class. """

#     def display_name(self):
#         print(self.name)    #public method

#         """Public Method (display_name): This method is also accessible from any part of the
#                          code. It directly accesses the public attribute and prints its value."""

# abc=public() 
# """Object (abc): An instance of Public is created, and the display_name method is called, 
#         demonstrating how public attributes and methods can be accessed directly."""

# abc.display_name()   #accessable
# print(abc.name)     # accessable



#Protected members : every things on ecapsulation.txt file
# class protected:
#     def __init__(self) -> None:
#         self._age=30

# class subclass(protected):  inheritates in subclass
#     def display(self):
#         print(self._age)

# abc=subclass()
# abc.display()


#private members:   every things on txt file 
# class private():
#     def __init__(self) -> None:
#         self.__salary=500000   #protection attribute

#     def salary(self):
#         print(self.__salary)  #access through the public method

# obj=private()
# print(obj.salary())   #work and access
# # print(obj.__salary())     

