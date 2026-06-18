# CREATE A ATM MACHINE  
print("Harsh RAj")
class Atm:
    
    __counter = 0

    def __init__(self):
        self.__pin = ""
        self.__balance= 0
        self.sno = Atm.__counter
        Atm.__counter = Atm.__counter+1
        self.__menu()
        

    def __menu(self):
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
                if ask_pin == self.__pin:
                    self.show_balance()  
                else:
                    print("you enter worng pin:")
            elif user == 3 :
                ask_pin= int(input("enter your pin"))
                if ask_pin == self.__pin:
                    deposit_amount = int(input("enter your deposit amount:"))
                    self.add_balance(deposit_amount)
                else:
                    print("you enter wrong pin:")
            elif user ==4 :
                ask_pin= int(input("enter your pin"))
                if ask_pin == self.__pin:
                    withdrawl_amount = int(input("enter your withdrawn amount:"))
                    self.widrowal_balance(withdrawl_amount)
                else:
                    print("you enter wrong pin:")
            elif user == 5:
                print('thanks: have good day')
                break
    
    @staticmethod
    def get_counter():
        return Atm.__counter
    @staticmethod
    def set_counter(new:int):
        if type(new)== int:
            Atm.__counter= new
        else:
            print("not allowed:")
    
    def get__pin(self):
        return self.__pin

    def set__pin(self,new_pin:str):
        if len(str(new_pin)) == 4:
            self.__pin = new_pin
        else:
            print("PIN must be 4 digits")
        
        
    def create_pin(self,pin):
        self.__pin = pin 
    def show_balance(self):
        print(f"your balance:{self.__balance}")

    def add_balance(self,deposit):
        self.__balance=self.__balance +  deposit
        print(f"₹{deposit} deposited successfully")
            
    def widrowal_balance(self,widrowal):
        if self.__balance < widrowal:
            print("balance is not availvel:")
        else:
            self.__balance= self.balance-widrowal
            print(f"₹{widrowal} withdrawn successfully.")

    
Sbi = Atm()
Hdfc= Atm()
Bob=Atm()



Atm.set_counter(0)
