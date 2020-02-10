#Palindrome_or_not
n=int(input("Enter number:"))
a=n
b=0
while(n>0):
    c=n%10
    b=b*10+c
    n=n//10
if(a==b):
    print("The number is a palindrome!")
else:
    print("The number isn't a palindrome!")
