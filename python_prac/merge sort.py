# define a function 
def merge_sort(left_arr,right_arr):
    i = 0
    j = 0
    # empty list 
    M = []
    # loop where i and j denoted the index of arr 
    while i < len(left_arr) and j < len(right_arr):
        # condition first 
        if left_arr[i] < right_arr[j]:
            M.append(left_arr[i])
            i = i+1

        else:
            M.append(right_arr[j])
            j = j+1
# when one side is sorted 
    while  i < len(left_arr): 
        M.append(left_arr[i])
        i = i+1
    while j < len(right_arr):
        M.append(right_arr[j])
        j = j+1
# return list 
    return M                

# it is dividing step 
def merge_conqr(arr):
    # must condition 
    if len(arr) <= 1:
        return arr
    # mid point 
    mid_indx = len(arr)//2
    left_side = arr[:mid_indx]
    right_side = arr[mid_indx:]
# recursion start 
    sorted_left = merge_conqr(left_side)
    sorted_right = merge_conqr(right_side)
# return left and right sorted 
    return merge_sort(sorted_left,sorted_right)

# main 
array = [12,11,1,90,56,3,22,77,8,45,1]
sorted_merge = merge_conqr(array)
print(sorted_merge)
