"""Problem 13 — Custom exception (medium)
Create a custom exception InsufficientFundsError. 
Add a withdraw(amount) method to UserAccount from problem 6 that raises this exception if amount exceeds balance."""

class InsufficientFundsError(Exception):
    pass
class UserAccount:
    def __init__(self):
        self.__balance=0

    def get_balance(self):
        return self.__balance
    
    def deposit(self,amount):
        self.__balance+=amount
        return self.__balance
    def withdraw(self,amount):
        if (self.__balance<amount):
            raise InsufficientFundsError("Amount exceeds balance")
        self.__balance -= amount
        return self.__balance


# Test cases
user = UserAccount()
print(user.get_balance())  # Should print 0
user.deposit(100)
print(user.get_balance())  # Should print 100


# Attempting direct access should fail
try:
    print(user.__balance)  # Should raise an AttributeError
except AttributeError:
    print("Cannot access private attribute __balance directly")

try:
    user.withdraw(200)  #Should raise an InsufficientFundsError
except InsufficientFundsError as e:
    print(e)

