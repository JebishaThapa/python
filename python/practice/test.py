#to split the array and add the first part to the endd
def split(arr, k):
    if k<=0 and k>=len(arr):
        return arr
    first_part = arr[:k]#means upto k which is 3
    second_part = arr[k:]#means after k which is after 3 
    result = second_part + first_part
    return result
print(split([1,2,3,4,5,6], 3))