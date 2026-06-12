# CREATE A ATM MACHINE  

class Atm:
    
    def __init__(self):
        self.pin = ""
        self.balance= 0
        self.menu()

    def menu(self):
        while True:
            user = int(input("""
    enter 1 create pin:
    enter 2 check balance:
    enter 3 add balance:
    enter 4 widroal balance:
    enter 5 to exit:                     
    """))

            if user == 1:
                enter_pin= int(input("enter your pin:"))
                self.create_pin(enter_pin)  
                print("create pin")
            elif user == 2:
                ask_pin= int(input("enter your pin"))
                if ask_pin == self.pin:
                    self.show_balance()  
                else:
                    print("you enter worng pin:")
            elif user == 3 :
                ask_pin= int(input("enter your pin"))
                if ask_pin == self.pin:
                    deposit_amount = int(input("enter your deposit amount:"))
                    self.add_balance(deposit_amount)
                else:
                    print("you enter wrong pin:")
            elif user ==4 :
                ask_pin= int(input("enter your pin"))
                if ask_pin == self.pin:
                    withdrawl_amount = int(input("enter your withdrawn amount:"))
                    self.widrowal_balance(withdrawl_amount)
                else:
                    print("you enter wrong pin:")
            elif user == 5:
                print('thanks have good day')
                break
            

        
    def create_pin(self,pin):
        self.pin = pin 
    def show_balance(self):
        print(f"your balance:{self.balance}")

    def add_balance(self,deposit):
        self.balance=self.balance +  deposit
        print(f"₹{deposit} deposited successfully")
            
    def widrowal_balance(self,widrowal):
        if self.balance < widrowal:
            print("balance is not availvel:")
        else:
            self.balance= self.balance-widrowal
            print(f"₹{widrowal} withdrawn successfully.")

    
sbi = Atm()

