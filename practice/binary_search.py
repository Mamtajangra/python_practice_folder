def binary_search(arr,val_find):
   low =0
   high = len(arr)
   while low < high:
        mid = (low+high)//2
        if val_find == arr[mid]:
            return mid
        if val_find < arr[mid]:
            high = mid-1
        else:
            low = mid+1 

 
array = [1, 2, 5, 12, 19, 33, 98]
value = 33
print(binary_search(array,value))