#Search if the word “learning” exists in the file or not.
word = "learning"
with open("A:\Study\Data Analyst\Python\Code\Problems Sagar\File Input & Output\practice.txt", "r") as f:
    data = f.read()
    
    if data.find(word):
        print("Found")
    else:
        print("Not Found.")