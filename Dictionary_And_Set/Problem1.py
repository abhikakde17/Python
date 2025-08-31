'''
WAP to enter marks of 3 subjects from the user and store them in a dictionary. Start with
an empty dictionary & add one by one. Use subject name as key & marks as value.
'''
marks = {}

a = int(input("Enter physics marks: "))
marks.update({"phy": a})

b = int(input("Enter english marks: "))
marks.update({"eng": b})

c = int(input("Enter maths marks: "))
marks.update({"maths": c})

print(marks)

