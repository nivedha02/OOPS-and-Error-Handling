"""Problem 14 — finally (easy)
Write a function read_file(filename) that opens and prints a file's contents. 
Use finally to always print "Finished attempting to read file." whether it succeeded or failed.
"""

def read_file(filename):
    try:
        with open(filename,"r",encoding='utf-8') as file:
            content=file.read()
            print(content)
    except FileNotFoundError:
        print("File not found")
    finally:
        print("Finished attempting to read file.")

read_file("File2.txt") #raises FileNotFoundError and finally statement
read_file("File1.txt") #reads file and finally statement
 