'''
Write a program to print the word "Python" in reverse using a FOR LOOP.

'''
word = "Python"

#As the length of the word is 6 and in python indexing starts from the 0,
# it only counts till 5 indexing so we used len(word) - 1 here.
for i in range(len(word)-1, -1, -1): 
    print(word[i], end=" ")
print()
    
#OR

for i in word[ : :-1]: #Here we directly used the indexing using word
    print(i , end=" ")