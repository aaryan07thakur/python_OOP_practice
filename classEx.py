class dog:
    species="canine"   #this is class attribute

    def __init__(self, name, age) -> None:
        self.name=name  #instance of attribute 
        self.age=age


#creating a object 
dog1=dog("buddy", 8)
dog2=dog("shera", 12)

print(dog1.species)   #Class variable
print(dog1.name,dog1.age, dog1.species)
print(dog2.name, dog2.age, dog2.species)
# print(dog1.age)
# print(dog2.age)



