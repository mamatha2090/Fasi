
n = int(input("Enter a non-negative integer: "))

if n < 0:
    print("Please enter a non-negative integer.")
else:
  
    factorial = 1
    for i in range(1, n + 1):
        factorial *= i
    
  
    print("Factorial of", n, ":", factorial)
