def find_duplicates(arr):
    duplicates = []

    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] == arr[j] and arr[i] not in duplicates:
                duplicates.append(arr[i])

    return duplicates

input_array = [1, 2, 3, 4, 5, 2, 7, 8, 4]
result = find_duplicates(input_array)

if result:
    print(f"The duplicate numbers are: {result}")
else:
    print("No duplicate numbers found.")
