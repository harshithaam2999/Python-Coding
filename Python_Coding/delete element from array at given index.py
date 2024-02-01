def delete_element_at_index(arr, index):
    if 0 <= index < len(arr):
        arr.pop(index)
        print(f"Element at index {index} deleted from the array.")
    else:
        print(f"Index {index} is out of bounds for the array.")

my_array = [1, 2, 3, 4, 5]
print("Original array:", my_array)

index_to_delete = int(input("Enter the index to delete: "))
delete_element_at_index(my_array, index_to_delete)

print("Array after deletion:", my_array)
