'''
Membership Operators

1. in 

2. not in 

'''


main_str = input("Enter a main string: ")
sub_str = input("Enter a sub-string: ")

if sub_str in main_str:
    print(f"{sub_str} is found in {main_str}")
    
else:
    print(f"{sub_str} is not found in {main_str}")
    
#Case Sensitive