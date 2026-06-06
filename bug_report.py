"""Problem 15 — Modules (medium)
Split your code into two files:
bug_report.py — contains the BugReport class
main.py — imports BugReport and creates 3 instances
Also add if __name__ == "__main__": in bug_report.py 
with a quick test that only runs when you execute that file directly, not when imported.

Split BugReport into its own file. Import and use it in main.py. Use if __name__ == "__main__": correctly.
# running bug_report.py directly:
Quick test: Bug: Test bug | Severity: low | Status: open
"""

class BugReport:
    def __init__(self, title, severity, status="open"):
        self.title = title
        self.severity = severity
        self.status = status
    
    def resolve(self):
        self.status = "closed"
    
    def summary(self):
        print(f"Bug: {self.title} | Severity: {self.severity} | Status: {self.status}")

if __name__=="__main__": #These will be called only if we call this bug_report file.
    print('Direct Call')
    test_bug=BugReport("Test bug","low")  
    test_bug.summary()
    test_bug.resolve()
