'''
Write a program to reverse each word in the sentence "Hello World" using a while loop.

'''
sentence = input("Enter a sentence = ")

words = sentence.split() #Here we split the sentence first.

for word in words:
    i = len(word)-1 #Here i is indexing number of the word.
    while i>=0:
        print(word[i], end=" ")
        i-=1