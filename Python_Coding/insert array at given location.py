arr=[1,2,3,4,5]
num=int(input("enter a number insert in array:"))
index=int(input("enter a index to insert value:"))
if index >= len(arr):
    print("please enter index snaller than",len(arr))
else:
    arr.insert(index,num)   
print("array after inserting ",num,arr)     

