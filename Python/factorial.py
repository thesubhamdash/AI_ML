def factorial(n):
    fact = 1
    for i in range(1,n+1):
        fact *= i
    
    return fact

n = int(input("Enter the value of n: "))

print(factorial(n))