# define a function having list and the value we want to find 
def linear_search(list1,val_to_find):
    # enumeration because we want to print value and index both 
    for index,value in enumerate(list1):
        # check firstly 
        if value == val_to_find:
            return(f"index is :{index}---> whose value is :{val_to_find}")
        # if value is from outside then print nothing 
    return "nothing"

        
    # main 
list1=[12,3,455,666,988,443,2321,222224,344,77889]
val_to_find=455
print(linear_search(list1,val_to_find))