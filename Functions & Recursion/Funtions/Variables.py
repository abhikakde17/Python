'''
Local Variables / Global Variables

Local Variables:
Variables which are defined inside the function.
Cannot be used outside the function

Global Variables:
Variables which are defined outside the function.
Can used outside the function.

'''

def xyz(a,b):
    a = 10
    b = 20
    c = a*b
    return c
d = xyz(10,30)
print(d)

