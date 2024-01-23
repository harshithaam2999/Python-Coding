arr1 = []
arr2 = []

n1=int(input("enter the size of arr1: "))
for i in range(n1):
    x=int(input(f"enter the {i+1} element of arr1:"))
    arr1.append(x)

n2=int(input("enter the size of arr2: "))
for i in range(n2):
    x=int(input(f"enter the {i+1} element of arr2: "))
    arr2.append(x)

if len(arr1)==len(arr2):
    print("array is equal")
else:
    print("array not equal")    
