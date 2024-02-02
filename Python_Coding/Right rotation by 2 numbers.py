def right_rotate(arr):
    n=len(arr)
    k=2

    rotated_array=arr[-k:] + arr[:-k]
    return rotated_array
original_array=[1,2,3,4,5,6]
result = right_rotate(original_array)

print("original array",original_array)
print("Array after right rotation is :",result)