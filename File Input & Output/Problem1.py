'''Create a new file “practice.txt” using python. Add the following data in it:

Hi Everyone
we are learning File I/O 
using python
i like programming in Python.'''


with open("practice.txt", "w") as f:
    f.write("Hi Everyone\nWe are learning file i/o\n") 
    f.write("Using Python\nI like programming in python.")