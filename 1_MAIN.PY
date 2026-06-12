# CREATE A ATM MACHINE  

class Atm:
    balance= 0

    def __init__(self):
        self.pin = ""
        self.balance= 0
        self.menu()

    def menu(self):
        while True:
            ask = int(input("""
    enter 1 create pin:
    enter 2 check balance:
    enter 3 add balance:
    enter 4 widroal balance:
    enter 5 to exit:                     
    """))

            if ask == 1:
                enter= int(input("enter your pin:"))
                self.create_pin(enter)  
                print("create pin")
            elif ask == 2:
                self.show_balance()  
            elif ask == 3 :
                deposit_amount = int(input("enter your deposit amount:"))
                self.add_balance(deposit_amount)
            elif ask ==4 :
                withdrawl_amount = int(input("enter your withdrawn amount:"))
                self.widrowal_balance(withdrawl_amount)
            else:
                exit
        
    def create_pin(self,pin):
        self.pin = pin 
    def show_balance(self):
        print(f"your balance:{self.balance}")

    def add_balance(self,deposit):
        self.balance=self.balance +  deposit
        print(f"₹{deposit} deposited successfully")
            
    def widrowal_balance(self,widrowal):
        self.balance= self.balance-widrowal
        print(f"₹{widrowal} withdrawn successfully.")

    
user= Atm()
