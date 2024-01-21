size=int(input("Enter the numbers:-"))
arr=[]
for i in range(0,size):
    num=int(input("enter the value for index "+str(i)+":"))
    arr.append(num)
average=sum(arr)/size
print("Average of array elements is ", average)





