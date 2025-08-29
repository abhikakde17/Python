'''
Create two list, take inputs from the user.
return  the common elements from these list

'''

def common():
    s1 = [1,2,8,4,5]
    s2 = [9,4,5,3,4,1]
 
#Here we use the SET build-in data type which returns the common elements.
    lst_1 = set(s1)
    lst_2 = set(s2)

    #For the commom elements we use the function

    commom_ele = lst_1.intersection(lst_2)
    print(commom_ele)

common()

