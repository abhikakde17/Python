'''
Write a program to count occurrences a specific character  in a string.

'''
string = input("Enter a string: ")
character_to_count = input("Enter the character to count: ")

count = 0
index = 0

while index < len(string):
    if string[index].lower() == character_to_count:#Herre we used .lower() to lowercase  the uppercase value.y
        count+=1
    index+=1
    
print(f"In {string}, '{character_to_count}' occures {count} times.")
      