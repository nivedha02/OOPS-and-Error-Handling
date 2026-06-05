"""Problem 12 — Multiple exceptions (medium)
Write a function parse_age(value) that converts a string to integer and checks it's between 0–120. 
Handle ValueError if it's not a number, and raise a custom InvalidAgeError if out of range."""

class InvalidAgeError(Exception):
    pass
def parse_age(value):
    try:
        x=int(value)
    except ValueError as e:
        raise ValueError("It's not a number")
    if  (x>120 or x<0):
       raise InvalidAgeError("out of range")
    return x

for value in [92, "k", "131"]:
    try:
        print(parse_age(value))
    except (ValueError, InvalidAgeError) as e:
        print(type(e).__name__, ":", e)


