'''WAF that replace all occurrences of “java” with “python” in above file.
'''

with open("A:\Study\Data Analyst\Python\Code\Problems Sagar\File Input & Output\practice.txt", "r") as f:
    data = f.read()
    
new_data = data.replace("Python", "Java")
print(new_data)

with open("A:\Study\Data Analyst\Python\Code\Problems Sagar\File Input & Output\practice.txt", "w") as f:
    f.write(new_data) #Overwriting the data.