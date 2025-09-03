'''
Write  a program to count the number of vowels in the word "Education" 

'''
vowels = "aeiou"
word = "education"
count = 0

#As we access  characters we use char
for char in word:
    if char in vowels:
        count+=1
        
print(f"The vowels in {word} is {count}.")