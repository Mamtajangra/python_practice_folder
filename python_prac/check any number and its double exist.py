# define a function double where we want to predict N=2*M 
def double(arr):
    # taking initial loop 
    for i in range(len(arr)):
        # another loop to check the condition 
        for j in range(len(arr)):
            # check condition if N=2*M
            if i!= j and  arr[i] == 2*arr[j]:
                #  condition true return true 
                return True
#  otherwise return false            
    return False        
# main array 
array  = [12,24,9,18]

print(double(array))
