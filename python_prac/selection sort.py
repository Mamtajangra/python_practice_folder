# define a function 
def selection_sort(arr):
    # length of array
    n = len(arr)
    # loop 
    for i in range(n):
        min_idx = i
        # another loop from i+1 to length of array 
        for j in range(i+1,n):
            if arr[j] < arr[min_idx]:
                # j is assigned to minimum index 
                min_idx = j
                # swapping minimum index with i 
        arr[i],arr[min_idx] = arr[min_idx],arr[i]


# main
array = [12,21,11,2,1,3,76,44,3]
selection_sort(array)
print(array)    