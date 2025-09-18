# here we will find out intersection of two arrays
def intersection_list(list1,list2):
    # firstly we will convert arr to set 
    set1 = set(list1)
    set2 = set(list2)
    # now find out the common element because intersection exist in set 
    print(list(set1 & set2))

# main 
list1 = [1,2,1,2,3,5,4]
list2 = [5,4,6,2,3,8]
# print result 
print(intersection_list(list1,list2))    