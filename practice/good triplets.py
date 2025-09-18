# from an array we will find out the count of good triplets via a,b,c term 
def good_triplet(arr,a,b,c):
    # initialize count is o \
    count = 0
    # using a loop over the arr 
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            for k in range(j+1,len(arr)):
                # check condition for good triplet 
                if abs(arr[i] - arr[j]) <=a and abs(arr[j] - arr[k]) <=b and abs(arr[i] - arr[k]) <=c:
                    count = count +1
    return count


# check 
arr = [3,0,1,1,9,7]
a = 7
b = 2
c = 3
print(good_triplet(arr,a,b,c))