# here we want to find out square root of a number just by binary search
def square_root(n):
    # suppose low point is 0
    low = 0
    # highest is n 
    high = n
    # through loop we will check condition low <= high 
    while low <= high:
        # now we find out mid index 
        mid = (low + high)//2
        # check condition if mid index is equal to n return
        if mid*mid == n:
            return mid
        # another condition if value towards left side the we will add 1 to the mid index 
        elif mid*mid < n:
            low = mid + 1
            # otherwise if it is in right side then decrease the mid by 1
        else:
            high = mid -1
    return mid            


# check 
n = 25
print(square_root(25))