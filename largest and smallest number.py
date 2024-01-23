arr=[]
n=int(input("enter the array size :"))
for i in range (n):
    x=int(input(f"enter the {i+1} elemements of array: "))
    arr.append(x)
largest=arr[0]
smallest=arr[0]
for i in range(n):
    if arr[i]>largest:
        largest=arr[i]
    if arr[i]<smallest:
        smallest=arr[i]  
print("largest element in array is ",largest)  
print("smallest element in array is ",smallest)            