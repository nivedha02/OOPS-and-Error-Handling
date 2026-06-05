"""Problem 7 — @property (medium)
Modify UserAccount from problem 6. Replace get_balance() with a 
@property called balance so you can access it like user.balance instead of user.get_balance()."""

class UserAccount:
    def __init__(self):
        self.__balance=0

    @property
    def balance(self):
        return self.__balance

    def deposit(self,amount):
        self.__balance+=amount
        return self.__balance

# Test cases
user = UserAccount()
print(user.balance)  # Should print 0
user.deposit(200)
print(user.balance)  # Should print 200

# Attempting direct access should fail
try:
    print(user.__balance)  # Should raise an AttributeError
except AttributeError:
    print("Cannot access private attribute __balance directly")