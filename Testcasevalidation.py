"""2. Test case class - easy
Create a TestCase class with name, expected, and actual attributes. Add a method passed() that returns True if expected equals actual, and a method result() that prints PASS or FAIL.
tc = TestCase("Login test", "Welcome, User!", "Welcome, User!")
tc.result()   # PASS: Login test
tc2 = TestCase("Price test", "99.00", "98.99")
tc2.result()  # FAIL: Price test"""
class TestCase:
    def __init__(self,name,expected,actual):
        self.name=name
        self.expected=expected
        self.actual=actual
    def passed(self):
        return(self.expected==self.actual)
    def result(self):
        if self.passed():
            print(f"PASS: {self.name}")
        else:
            print(f"FAIL: {self.name}")
tc = TestCase("Login test", "Welcome, User!", "Welcome, User!")
tc.result()   # PASS: Login test
tc2 = TestCase("Price test", "99.00", "98.99")
tc2.result()  # FAIL: Price test
