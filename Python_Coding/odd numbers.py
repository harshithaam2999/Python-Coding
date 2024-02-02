def odd_numbers(arr):
    for num in arr:
        if num%2 != 0:
            print(num)
arr=[1,2,3,4,5,6,7,8,9,10]
print("odd numbers in the array",arr)
odd_numbers(arr)         