# Input two numbers
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

def gcd(x, y):
    while y != 0:
        x, y = y, x % y
    return x

result = gcd(a, b)
print(f"GCD of {a} and {b} is {result}")
