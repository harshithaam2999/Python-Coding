n1=int(input("enter the first number n1:"))
n2=int(input("enter the second number n2:"))
n3=int(input("enter the third number n2:"))

if (n1>=n2) and (n1>=n3):
    largest=n1
    if (n2>=n1) and (n2>=n3):
       largest=n2
else:
    largest=n3
    print("the largest number is ,largest")


   