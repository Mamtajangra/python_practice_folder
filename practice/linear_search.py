def linear_search(arr, val_to_find):
    for i in range(len(arr)):
        if val_to_find == arr[i]:
            return i
array = [12,21,11,96,34,21]
value =11
print(linear_search(array,value))       