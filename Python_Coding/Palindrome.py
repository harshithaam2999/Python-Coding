n=int(input("enter the number:\n"))
reverse,temp=0,n
while temp!=0:
    reverse=reverse*10+temp%10;
    temp=temp//10;
if reverse ==n:
    print("***The given number is palindrome***")
else:
    print("***The given number is not plindrome***")
