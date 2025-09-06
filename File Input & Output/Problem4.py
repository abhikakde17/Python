'''
WAF to find in which line of the file does the word “learning”occur first.
Print -1 if word not found.
'''

def check_for_word():
    word = "learning"
    data = True
    line_no = 1
    with open("A:\Study\Data Analyst\Python\Code\Problems Sagar\File Input & Output\practice.txt", "r") as f:
        while data:
            data = f.readline()
            if word in data:
                print(line_no)
            line_no+=1
    
    return -1
check_for_word()