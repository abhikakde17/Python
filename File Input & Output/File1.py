#File Input/Output

#Python can be used to perform operations on a file. (read & write data)

#We have to open a file before reading or writing.

# f = open("file_name", "mode") mode such as read or write


f = open("A:\Study\Data Analyst\Python\Code\Problems Sagar\File Input & Output\demo.txt", "r")
data = f.read()
print(data)
print(type(data))
f.close()