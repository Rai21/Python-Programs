# 1. Loops: Check if a number is prime using a loop.

def is_prime(num):
    if num <= 1:
        return False
    for i in range(2,int(num ** 0.5)+1):
        if num % i == 0:
            return False
    return True
# User Input
number = int(input("Enter Number: "))
if is_prime(number):
    print(f"{number} is prime Number")
else:
    print(f"{number} is not prime Number")
