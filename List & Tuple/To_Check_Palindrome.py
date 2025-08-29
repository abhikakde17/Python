#WAP to check if a list contains a palindrome of elements.

'''A palindrome is a word, number, phrase, or sequence of characters
 that reads the same forward and backward, ignoring spaces,punctuation, and letter case.
'''

list1 = [1,2,3,2,1]

copy_list1 = list1.copy()
copy_list1.reverse()

if (copy_list1 == list1):
    print("Palindrome.")
else:
    print("NOT Palindrome.")
