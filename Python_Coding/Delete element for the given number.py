def delete_element(arr, element):
    if element in arr:
        arr.remove(element)
        print(f"Element {element} deleted from the array.")
    else:
        print(f"Element {element} not found in the array.")

array = [1, 2, 3, 4, 5]
print("Original array:", array)

element_to_delete = int(input("Enter the element to delete: "))
delete_element(array, element_to_delete)

print("Array after deletion:", array)
