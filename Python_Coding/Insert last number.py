def insert_at_end(arr, element):
    arr.append(element)

list = [1, 2, 3, 4, 5]
new_element = 6

print("Original array:", list)
insert_at_end(list, new_element)
print("Array after inserting element at the end:", list)
