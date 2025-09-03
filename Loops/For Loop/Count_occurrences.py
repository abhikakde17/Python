'''
Write a program to count occurrences of each character in the word "Programming.
'''

word = "Programming"
char_count = {}

for char in word:
    if char in char_count:
        char_count[char] +=1
    else:
        char_count[char] = 1
        
for char, count in char_count.items():
    print(char + ':', count)