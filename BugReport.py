class BugReport:
    def __init__(self, title, severity, status="open"):
        self.title = title
        self.severity = severity
        self.status = status
    
    def resolve(self):
        self.status = "closed"
    
    def summary(self):
        print(f"Bug: {self.title} | Severity: {self.severity} | Status: {self.status}")

# Test cases
bug = BugReport("Login fails on Safari", "high")
bug.summary()    # Bug: Login fails on Safari | Severity: high | Status: open
bug.resolve()
bug.summary()    # Bug: Login fails on Safari | Severity: high | Status: closed

# Test with different bug report
bug2 = BugReport("Checkout error on mobile", "medium")
bug2.summary()   # Bug: Checkout error on mobile | Severity: medium | Status: open
