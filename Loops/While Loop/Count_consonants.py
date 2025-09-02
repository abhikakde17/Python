'''
Write a program to count the number of consonants on the word "Learning" 

'''

word = input("Enter a word to check: ")

count = 0
vowels = "aeiou"
index = 0

while index < len(word):
    #.lower() used in case user gives a uppercase value.
    #.isaplha() checks whether the input is aplhabate or not.
    if word[index].lower() not in vowels and word[index].isalpha():
        count+=1
    index+=1
print(f"Number of Consonants: {count}")