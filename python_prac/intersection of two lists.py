# define a function 
def intersection(list1,list2):
    # remove duplicates from list1,2 using set 
    set1 = set(list1)
    set2 = set(list2)
# now intersection between two sets 
    intersection_list = set1 &set2
    # convert this set into list and return 
    return list(intersection_list)


# main
list1 = [1,2,3,2,4,7,8,4,5,3]
list2 = [2,4,5,3,8,9]
print(intersection(list1,list2))