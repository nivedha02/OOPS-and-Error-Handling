"""Problem 6 — Encapsulation with private attribute (medium)
Create a UserAccount class with a private attribute __balance. 
Add a get_balance() method to read it and a deposit(amount) method to add to it. 
Direct access like user.__balance should not work."""

class UserAccount:
    def __init__(self):
        self.__balance=0

    def get_balance(self):
        return self.__balance
    
    def deposit(self,amount):
        self.__balance+=amount
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
