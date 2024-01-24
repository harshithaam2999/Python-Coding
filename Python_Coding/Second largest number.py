def second_largest(array):
    if len(array) < 2:
        return "Array should have at least two elements"

    array.sort(reverse=True)
    return array[1]

array = []
n = int(input("Enter the number of elements: "))

for i in range(n):
    x = int(input(f"Enter the {i+1}st element: "))
    array.append(x)

result = second_largest(array)
print("Second largest number in the array is:", result)