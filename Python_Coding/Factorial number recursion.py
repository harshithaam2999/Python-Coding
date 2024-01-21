def factorial(n):
    if n==1:
        return 1
    else:
        return n*factorial(n-1)
num=int(input("enter the number:"))
if num < 0:
    print("the factorial can not be calculated")
elif num == 0:
    print("the factorial of 0 is 1") 
else:
    print("Factorial of num is" , factorial(num))       



    