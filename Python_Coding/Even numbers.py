def print_even_numbers(arr):
    for num in arr:
        if num % 2 == 0:
            print(num)

array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("Even numbers in the array:")
print_even_numbers(array)
