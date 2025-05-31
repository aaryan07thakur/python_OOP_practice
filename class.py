# class Atm:
#     def __init__(self): #  here __init__ is a constructor. it is a special method that 
#                                 # initializes the object when it is created.in python, constructor
#                                 # name is always __init__.
#         # self.balance=0
#         # self.pin=""

#         print("welcome to the ATM")

# NICA=Atm()     #this is object 
        


class Atm:
    def __init__(self) -> None:
        self.balance = 0
        self.pin = ""
        self.menu()
        # self.create_pin()
        # self.diposit()
        # self.withdraw()
        # self.check_balance()
        
            
    
    def menu(self):
        while True:
            user_input=input(""" Hello, how would you like to proceed?
                            1. Enter 1 to create a pin
                            2. Enter 2 to diposit
                            3. Enter 3 to withdraw
                            4. Enter 4 to check balance
                            5. Enter 5 to exit
        """)
            
            if user_input =="1":
                self.create_pin()
            elif user_input=="2":
                self.deposit()
            elif user_input=="3":
                self.withdraw()
            elif user_input=="4":
                self.check_balance()
            elif user_input=="5":
                print("Thank you")
                break
            else:
                print("bye")


    def create_pin(self):
        self.pin=input("create a pin: ")
        print("your pin is created successfully")

    def deposit(self):
        temp=input("Enter your pin: ")
        if temp==self.pin:
            amount=int(input("Enter the amount you want to diposit: "))
            self.balance=self.balance +amount
            print("diposit successfully")
            print(f"YOur new balance is {self.balance}")
        else:
            print("Invalid pin! Please Enter the valid pin")

    def withdraw(self):
        temp=input("Enter your pin: ")
        if temp==self.pin:
            amount=int(input("Enter the amount you wnat to withdraw: "))  
            if amount<= self.balance:
                self.balance=self.balance-amount
                print("Withdrawal successful.")
                print(f"Your remaining balance is: {self.balance}")
            else:
                print("insufficient balance")
        else:
            print("invalid pin. Please Enter the valid pin")
    

    def check_balance(self):
        temp= input("Enter your pin: ")
        if temp== self.pin:
            print(f"your new balance is: {self.balance}")
        else:
            print("invalid pin")

                    


abc=Atm()