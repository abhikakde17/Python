
f = open("A:\Study\Data Analyst\Python\Code\Problems Sagar\File Input & Output\demo.txt", "r")

data = f.read(5) #Returns the first 5 characters.
print(data)

line1 = f.readline() #Returns the first line.
print(line1)