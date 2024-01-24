def remove_duplicates(arr):
    elements=[]
    for num in arr:
        if num !=elements:
            elements.append(num)
    return elements
array=[]
n=int(input("enter the array size:"))
for i in range (n):
    x=int(input(f"enter the {i+1}st element:"))
    array.append(x)
result=remove_duplicates(array)    
print("Array before removing duplicates:",result)
            