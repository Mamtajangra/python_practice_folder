def perfect_sq(num):
    # we check from 1 to integer values 
    low = 1
    high = num
    # low always less than high 
    while low <= high:
        # mid index 
        mid =(low+high)//2
        # if this value(mid)*mid is result we get true 
        if mid*mid == num:
            return True
        # but in left side we should increase the value of low because here we are not searching proper element but we try to reach nearby the num value 
        elif mid*mid < num:
            # ex = 3*3 = 9 but num = 16 so we try to change the position of low instead of high because high is num which is fix 
            low = mid+1
            # otherwise thi scase arise 
        else:
            high =mid-1
    return False


num = 16
print(perfect_sq(num))



