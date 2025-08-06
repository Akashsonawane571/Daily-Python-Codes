'''

Write a function to calculate the factorial of a number.

The factorial of a non-negative integer n is the product of all positive integers less than or equal to n.
For example, if n is 5, the return value should be 120 because 1*2*3*4*5 is 120.

'''

def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

num = int(input("Enter your number: "))
print("Factorial of", num, "is", factorial(num))

'''
output
Enter your number: 10
Factorial of 10 is 3628800

=== Code Execution Successful ===
'''

