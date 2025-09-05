#Write a Recursive function to print all elements in a list.

def print_list(list, idx=0):
    if idx == len(list):
        return
    print(list[idx])
    print_list(list, idx+1)

fruits = ["mango", "graphes", "apple", "pineapple", "banana"]

print_list(fruits)