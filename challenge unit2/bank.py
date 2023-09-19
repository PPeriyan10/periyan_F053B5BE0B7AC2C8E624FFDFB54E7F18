class BankAccount:
  def __init__(self,account_number, account_holder_name , initial_balance=0.0):
    self.__account_number=account_number
    self.__account_holder_name=account_holder_name
    self.__account_balance=initial_balance

  def deposit(self,amount):
    if amount >0 :
      self.__account_balance+=amount
      print("deposited ₹{}.new balance: ₹{}".format (amount, self.__account_balance))
    else:
      print("invalid deposit amount ,please deposit a positive amount.")
      
  def withdraw (self , amount):  
    if amount >0:
      if amount<= self.__account_balance:
        self.__account_balance-=amount
        print("withdrew ₹{}.NEW balance:₹{}".format(amount,self.__account_balance))
      else:
        print("invaild withdraw.")
    else:
      print("please enter valid amount.")

  def display_balance(self):
    print("Account balance₹{}(account #{}):₹{}".format(self.__account_holder_name,
                                                       self.__account_number,
                                                       self.__account_balance))
account = BankAccount(account_number="1234556789",
                      account_holder_name="---------",
                       initial_balance=5000.0)   
account.display_balance()
account.deposit(5000)
account.withdraw(200)
account.display_balance()
account.withdraw(500)
account.deposit(100)
account.display_balance()