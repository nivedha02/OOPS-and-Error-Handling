"""Problem 3 — TestSuite class
Create a TestSuite class that holds a list of TestCase objects. Add add(tc), run(), 
and summary() methods.
suite = TestSuite()
suite.add(TestCase("Login", "200", "200"))
suite.add(TestCase("Logout", "200", "404"))
suite.add(TestCase("Home", "welcome", "welcome"))
suite.run()
# PASS: Login
# FAIL: Logout
# PASS: Home
suite.summary()
# Passed: 2 | Failed: 1"""

from Testcasevalidation import TestCase
class TestSuite:
    def __init__(self):
        self.list1=[]
        self.Passed=0
        self.Failed=0
    def add(self,tc):
        self.list1.append(tc)
        
    def run(self):
        for i in self.list1:
            if (i.passed()):
                self.Passed+=1
            else:
                self.Failed+=1

    def summary(self):
        print(f"Passed: {self.Passed} | Failed: {self.Failed}")

suite = TestSuite()
suite.add(TestCase("Login", "200", "200"))
suite.add(TestCase("Logout", "200", "404"))
suite.add(TestCase("Home", "welcome", "welcome"))
suite.run()
suite.summary()
    


