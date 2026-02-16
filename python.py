class industry:
    def __init__(self, name,country,owner):
        self.name=name
        self.country=country
        self.owner=owner
    def instrument(self):
        print("sugar mill")
class owner:
    def __init__(self,name,adress,contact_num,stock_available):
        self.name=name
        self.adress=adress
        self.contact_num=contact_num
        self.stock_available=stock_available
owner1=owner("alysami","bwp_Rod_pak",+923222222,"sugar_all_stock_available_breed_choclate_birthday_cakes")       
industry1=industry("al_hafiz_sugar_mill","pakistan",owner1)
print("industry_name=",industry1.name)
print("country=",industry1.country)
print("owner=",industry1.owner.name)
print("ADRESS=",industry1.owner.adress)
print("phone_num=",industry1.owner.contact_num)
print("stock=",industry1.owner.stock_available)


# start 35 minutes to 40 minutes

class user:
    def __init__(self, email,password,username):
        self._email=email
        self.password=password
        self.username=username
    def say_hi_to_user(self,user):
            print(f"sending message to {user.username}: hi {user.username}, my nameis {self.username}")
user1=user("hammadlatif@gmail.com","7654368","saminagari")
user2=user("shahzaib@gmail","8888888","shahzaib")
user1.say_hi_to_user(user2)

# how to update value 

class user:
    def __init__(self, email,password,username):
        self._email=email
        self.password=password
        self.username=username
    def say_hi_to_user(self,user):
            print(f"sending message to {user.username}: hi {user.username}, my nameis {self.username}")
user1=user("saminagari15@gmail.com","709575","saminagari")
print(user1._email)
user1._email="alys@gmail.com"
print(user1._email)


# get method

class user:
    def __init__(self, email,password,username):
        self._email=email
        self.password=password
        self.username=username
    def get_email(self):
        return self._email
    
user1=user("get_email:""saminagari15@gmail.com","712370","saminagri")
print(user1.get_email())
# clean method
class user:
    def __init__(self, email,password,username):
        self._email=email
        self.password=password
        self.username=username
    def clean_email(self):
        return self._email
    
user1=user("clean_email:""alisami.com","1234570","alisami")
print(user1._email)
print(user1.clean_email())

# set email method
from datetime import datetime
class user:
    def __init__(self, email,password,username):
        self._email=email
        self.password=password
        self.username=username
    def get_email(self):
        print(f" Email Accessed:{datetime.now()}")
        return self._email
    def set_email(self,new_email):
        if "@" in new_email:
            self._email=new_email
        else:
            print("Invalid email")
        
    
    
user1=user("saminagari15@gmail.com","1234570","saminagari")
print(user1.get_email())


user1.set_email("alysami21@email.com")
print(user1.get_email())


class user:
    def __init__(self, email,password,username):
        self._email=email
        self.password=password
        self.username=username
        @property
        def email(self):
            print("email accessed")
            return self._email
        @email.setter
        def email(self,new_email):
            if "@" in new_email:
                self._email=new_email
    
        
        
user1=user("saminagari15@gmail.com","1234750","saminagari")
user1._email="not email"
print(user1._email)



# static attributes


class User:
    user_count = 0   # class variable

    def __init__(self, email, username):
        self._email = email
        self.username = username
        User.user_count += 1  

    def display_user(self):
        print(f"Username: {self.username}, Email: {self._email}")


user1 = User("saminagari15@gmail.com", "saminagari")
user2 = User("shahzaib@gmail.com", "shahzaib")

print(User.user_count)
print(user1.user_count)
print(user2.user_count)



class BankAccount:
    Min_balance = 100

    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if self.is_valid_amount(amount):
            self.balance += amount
            self.__log_transaction("deposit", amount)
        else:
            print("Deposit amount must be positive")

    def is_valid_amount(self, amount):
        return amount > 0

    # private method
    def __log_transaction(self, transaction_type, amount):
        print(f"Logging {transaction_type} of ${amount}. New balance: ${self.balance}")

    @staticmethod
    def is_valid_interest_rate(rate):
        return 0 <= rate <= 100


# object create
account = BankAccount("sami", 500)

# deposit
account.deposit(200)

# valid amount check
print(account.is_valid_amount(200))

# static method call
print(BankAccount.is_valid_interest_rate(5))
print(BankAccount.is_valid_interest_rate(10))

# encapsulattion
class BankAccount:
    def __init__(self, balance):
        self.balance=balance
        
        
account=BankAccount(0)
account.balance=-1
print(account.balance)

# class BankAccount:
    #def __init__(self):
     
    #self._balance = 0.0  # private variable

   # @property
    #def balance(self):
       # return self._balance

    #def deposit(self, amount):
        #if amount <= 0:
           # raise ValueError("Deposit amount must be positive")
        #self._balance += amount

    #def withdraw(self, amount):
        #if amount <= 0:
           # raise ValueError("Withdrawal amount must be positive")
       # if amount > self._balance:
          #  raise ValueError("Insufficient funds.")
        #self._balance -= amount

# Usage
#account = BankAccount()
#print(account.balance)  # Output: 0.0

#account.deposit(1.99)
#account.withdraw(1)
#print(account.balance)  # Output: 0.99

# This will raise an error
#account.withdraw(100)   # ValueError: Insufficient funds.

class BankAccount:
    def __init__(self):
        self._balance = 0.0  # private variable

    @property
    def balance(self):
        return self._balance

    def deposit(self, amount):
        if amount <= 0:
            print("Deposit amount must be positive!")
            return False
        self._balance += amount
        print(f"Deposited: {amount}. New balance: {self._balance}")
        return True

    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal amount must be positive!")
            return False
        if amount > self._balance:
            print("Insufficient funds!")
            return False
        self._balance -= amount
        print(f"Withdrew: {amount}. New balance: {self._balance}")
        return True


# Usage outside the class
account = BankAccount()
print(f"Initial balance: {account.balance}")

account.deposit(1.99)
account.withdraw(1)
print(f"Balance after transactions: {account.balance}")

account.withdraw(100)
print(f"Final balance: {account.balance}")

