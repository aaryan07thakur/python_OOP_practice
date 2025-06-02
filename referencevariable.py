#note: class ko object are mutaible like list, distanary and sets

class customer:
    def __init__(self, name, gender) -> None:
        self.name=name
        self.gender=gender
    
def greeting(customer):
        if customer.gender=="male":
            print("Hello",customer.name, "sir")
        else:
             print("hello",customer.name, "mam")


cust=customer("nandu", "female")
# print(cust.name)
greeting(cust)  #calss ko function ma object pass gare ko that is boject=cust

        