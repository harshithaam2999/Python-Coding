def reverse_array(arr):
    start = 0
    end = len(arr) - 1

    while start < end:
       
        arr[start], arr[end] = arr[end], arr[start]
        
        start = 0
        end = 0

list = [1, 2, 3, 4, 5]
print("Original array:", list)

reverse_array(list)
print("Reversed array:", list)
