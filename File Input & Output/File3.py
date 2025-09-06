#with Syntax

'''
with open ("file name", "mode") as f:
        data = f.read
        

'''

with open ("A:\Study\Data Analyst\Python\Code\Problems Sagar\File Input & Output\demo.txt","r") as f:
    data = f.read()
    print(data) 
    
#Automatically closes the file.

with open("A:\Study\Data Analyst\Python\Code\Problems Sagar\File Input & Output\demo.txt", "w") as f:
    f.write("i'm an engineer.")