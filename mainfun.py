from bug_report import BugReport
print("Using Functions from bug_report via import only 3 instance are called")
bug1 = BugReport("Login button not working", "High")
bug2 = BugReport("Page loads slowly", "Medium")
bug3 = BugReport("Typo in footer", "Low")

bug1.summary() #Bug: Login button not working | Severity: High | Status: open
bug1.resolve() #Changes Status
bug1.summary() #Bug: Login button not working | Severity: High | Status: 

bug2.summary() #Bug: Page loads slowly | Severity: Medium | Status: open
bug2.resolve()
bug2.summary() #Bug: Page loads slowly | Severity: Medium | Status: closed

bug3.summary() #Bug: Typo in footer | Severity: Low | Status: open
bug3.resolve()
bug3.summary() #Bug: Typo in footer | Severity: Low | Status: closed
