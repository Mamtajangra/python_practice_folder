# define a function.. here we want to find single element from the array where each number are twice except one and we want to find that number
def single_element(arr):
# suppose initially there is 0 number
    result = 0
    # apply a loop on array and using each index
    for i in arr:
# to remove duplicate and findout unique number we use  XOR  here according to XOR same bit give 0 and different gives 1
        result ^= i 
        # return result 
    return result

# main 
arr = [1,2,1,2,3,5,5,4,6,6,4]
print(single_element(arr))