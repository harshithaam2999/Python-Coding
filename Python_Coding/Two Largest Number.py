def two_largest_numbers(arr):
    if len(arr) < 2:
        return "Array should have at least two elements"
    max1 = max2 = float('-inf')

    for num in arr:
        if num > max1:
            max2 = max1
            max1 = num
        elif num > max2 and num != max1:
            max2 = num

    return max1, max2

array = [12, 4, 7, 9, 15, 8]
result = two_largest_numbers(array)

print("Two largest numbers in the array:", result)
