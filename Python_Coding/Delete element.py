def delete_element_at_end(arr):
    if len(arr) == 0:
        return"Array is empty cannot delete from an empty array"
    arr.pop()
array=[1,2,3,4,5]
print("original array",array)  
delete_element_at_end(array)
print("array after deleting element at the end is :",array)  