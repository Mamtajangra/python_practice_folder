'''loop from 0 to len(arr)
fixed curr val as arr[i]
check curr val is smaller than the previous one  if yes 
previous value = next value also check it with the remaining values present in the left side finall that j+1 fixed as curr val'''


# define a function 
def insertion_sort(arr):
# length of array 
    n = len(arr)
    # loop from 1 to n 
    for i in range(1,n): 
        # decide current value
        curr_val = arr[i]
        # previous element of i 
        j = i - 1
        # use because we don't know the steps here 
        while curr_val < arr[j] and j >= 0:
            # fill the empty portion 
            arr[j+1] = arr[j]
            # also check the previous elements 
            j = j-1
            # j+1 is curr value now 
            arr[j+1] = curr_val




# main
array = [12,21,11,2,1,3,76,44,3]
insertion_sort(array)
print(array)    