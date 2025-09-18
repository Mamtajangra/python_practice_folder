# here we will find the distance between arrays and count the distance which is less than the target value 
def distance(arr1,arr2,val):
    # initially count is 0
    count = 0
    # loop over arr1 
    for i in range(len(arr1)):
        # let result is true for all i 
        result = True
        # second loop over arr2 
        for j in range(len(arr2)):
            # let difference is M 
            M = abs(arr1[i] - arr2[j])
            # check condition 
            if M <= val:
                result = False
                # for every false break the statement 
                break
        #   check M is greater than value 
        if M>val:
            result = True
            count = count+1
    return count




arr1 = [1,2,3,5,4,7,6]
arr2 = [7,8,4,3,5,9,3]
val =1
print(distance(arr1,arr2,val))