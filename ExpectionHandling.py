"""Problem 11 — try/except (easy)
Write a function divide(a, b) that returns a / b but catches ZeroDivisionError and 
prints "Cannot divide by zero" instead of crashing.
"""
def divide(a,b):
    try:
        x=a/b
        print(x)
    except ZeroDivisionError:
        print("Cannot divide by zero")

divide(5,3) # 1.6666666666666667
divide(4,0) # Cannot divide by zero