def recursive_factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * recursive_factorial(n - 1)
n = int(input("Enter a number: "))
print("Factorial:", recursive_factorial(n))