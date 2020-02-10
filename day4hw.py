#using recursion
def Fibrec(n):  
   if n <= 1:  
       return n  
   else:  
       return(Fibrec(n-1) + Fibrec(n-2))  
nt = int(input("Enter the terms? "))   
print("Fibonacci series are:")  
for i in range(nt):  
    print(Fibrec(i))

#factorial of number
fact = 1
num = int(input("Enter a number: "))
fact = 1
for i in range(1,num + 1):
    fact = fact*i
print("The factorial of",num,"is",fact)