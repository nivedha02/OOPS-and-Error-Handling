"""Problem 5 — Class variable (easy)
Add a class variable count to BugReport that tracks 
how many bug instances have been created. 
Every time a new bug is created, count goes up by 
1. Print BugReport.count after creating 3 bugs — should print 3."""

class BugReport:
    count=0
    def __init__(self, title, severity, status="open"):
        self.title = title
        self.severity = severity
        self.status = status
    
    def resolve(self):
        self.status = "closed"
    
    def summary(self):
        print(f"Bug: {self.title} | Severity: {self.severity} | Status: {self.status}")
        BugReport.count+=1
 

# Test cases
bug = BugReport("Login fails on Safari", "high")
bug.summary()    # Bug: Login fails on Safari | Severity: high | Status: open
bug.resolve()
bug.summary()    # Bug: Login fails on Safari | Severity: high | Status: closed
print("No of bugs created:", BugReport.count)  # Should print 2

# Test with different bug report
bug2 = BugReport("Checkout error on mobile", "medium")
bug2.summary()   # Bug: Checkout error on mobile | Severity: medium | Status: open

print("No of bugs created:", BugReport.count)  # Should print 3