# DEFINE A FUNCTION 
def sort_indices(arr,value):
# FIRSTLY SORT AN ARRAY 
    arr.sort()
    # TAKING AN EMPTY LIST 
    M = []
    # LOOP OVER THE ARRAY 
    for i in range(len(arr)):
        # CHECK THE VALUE WITH EACH ELEMENTS 
        if value == arr[i]:
        #    IF VALUE OCCUR EASILY APPEND IT TO M 
           M.append(i)
        #    RETURN THE LIST 
    return M       




# MAIN 
array = [1,3,2,4,2,3,7,2,3]
value = 3
    # print(X)
print(sort_indices(array,value))           