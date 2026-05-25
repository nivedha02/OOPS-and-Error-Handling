Problem 3 — Classes and objects (medium)
Create a TestSuite class with an empty list on creation. Add methods: add(tc) adds a TestCase, run() calls result() on every test, summary() prints passed and failed count.

Problem 4 — __str__ method (easy)
Add a __str__ method to BugReport so that print(bug) automatically shows Bug: {title} | Severity: {severity} | Status: {status} without calling .summary().

Problem 5 — Class variable (easy)
Add a class variable count to BugReport that tracks how many bug instances have been created. Every time a new bug is created, count goes up by 1. Print BugReport.count after creating 3 bugs — should print 3.

Problem 6 — Encapsulation with private attribute (medium)
Create a UserAccount class with a private attribute __balance. Add a get_balance() method to read it and a deposit(amount) method to add to it. Direct access like user.__balance should not work.

Problem 7 — @property (medium)
Modify UserAccount from problem 6. Replace get_balance() with a @property called balance so you can access it like user.balance instead of user.get_balance().

Problem 8 — Inheritance (medium)
Create a base class Animal with name and a method speak() that prints "...". Create two child classes Dog and Cat that override speak() — Dog prints "Woof!", Cat prints "Meow!".

Problem 9 — super() (medium)
Create a base class Employee with name and salary. Create a child class Manager that adds a team_size attribute. Use super().__init__() in Manager to avoid repeating the parent's init code.

Problem 10 — Polymorphism (medium)
Create three classes Circle, Rectangle, Triangle — each with an area() method. Write a function print_areas(shapes) that takes a list of any mix of these objects and prints each area. Same function, different behaviour per object.

Problem 11 — try/except (easy)
Write a function divide(a, b) that returns a / b but catches ZeroDivisionError and prints "Cannot divide by zero" instead of crashing.

Problem 12 — Multiple exceptions (medium)
Write a function parse_age(value) that converts a string to integer and checks it's between 0–120. Handle ValueError if it's not a number, and raise a custom InvalidAgeError if out of range.

Problem 13 — Custom exception (medium)
Create a custom exception InsufficientFundsError. Add a withdraw(amount) method to UserAccount from problem 6 that raises this exception if amount exceeds balance.

Problem 14 — finally (easy)
Write a function read_file(filename) that opens and prints a file's contents. Use finally to always print "Finished attempting to read file." whether it succeeded or failed.

Problem 15 — Modules (medium)
Split your code into two files:

bug_report.py — contains the BugReport class
main.py — imports BugReport and creates 3 instances

Also add if __name__ == "__main__": in bug_report.py with a quick test that only runs when you execute that file directly, not when imported.

Your progress: 2/15
Solve them in order — each one builds on the last. Paste your code here and I'll review it right away.You said: give as description and outputgive as description and output9:49 PMClaude responded: Here you go — all 15, description and expected output only, no hints, no solutions:Here you go — all 15, description and expected output only, no hints, no solutions:

Problem 1 ✅ Done
Problem 2 ✅ Done

Problem 3 — TestSuite class
Create a TestSuite class that holds a list of TestCase objects. Add add(tc), run(), and summary() methods.
PASS: Login
FAIL: Logout
PASS: Home
Passed: 2 | Failed: 1

Problem 4 — __str__ method
Add __str__ to BugReport so printing the object directly shows its details.
Bug: Dark mode broken | Severity: low | Status: open

Problem 5 — Class variable
Add a class variable count to BugReport that tracks total instances created.
3

Problem 6 — Private attribute
Create UserAccount with a private __balance. Add get_balance() and deposit(amount).
1000
1500

Problem 7 — @property
Modify UserAccount so balance is accessed like an attribute, not a method call.
1000
1500

Problem 8 — Inheritance
Base class Animal with speak(). Child classes Dog and Cat override it.
Woof!
Meow!

Problem 9 — super()
Base class Employee with name and salary. Child class Manager adds team_size using super().
Manager: Arun | Salary: 80000 | Team size: 5

Problem 10 — Polymorphism
Three classes Circle, Rectangle, Triangle each with area(). One function handles all three.
Circle area: 78.54
Rectangle area: 24
Triangle area: 10.0

Problem 11 — try/except
Function divide(a, b) handles division by zero gracefully.
5.0
Cannot divide by zero

Problem 12 — Multiple exceptions
Function parse_age(value) handles invalid input and out of range values.
25
Not a number: abc
Invalid age: 150. Must be between 0 and 120.

Problem 13 — Custom exception
withdraw(amount) on UserAccount raises InsufficientFundsError if amount exceeds balance.
Withdrew 200. Remaining balance: 800
Insufficient funds: tried to withdraw 1500, balance is 800

Problem 14 — finally
Function read_file(filename) always prints a closing message.
<file contents here>
Finished attempting to read file.

# when file missing:
File not found.
Finished attempting to read file.

Problem 15 — Modules
Split BugReport into its own file. Import and use it in main.py. Use if __name__ == "__main__": correctly.
# running bug_report.py directly:
Quick test: Bug: Test bug | Severity: low | Status: open

# running main.py:
Bug: Login broken | Severity: high | Status: open
Bug: UI glitch | Severity: low | Status: open
Bug: API timeout | Severity: medium | Status: open

Your progress: 2/15 done.
Start from problem 3 and paste your code. I'll review immediately.
