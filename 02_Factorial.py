# 2. Loops: Find the factorial of a number using a loop

def Factorial(num):
    if num < 1:
        return "Negativ number is not allowed"
    result = 1
    for i in range(1,num +1):
        result *=i
    return result

number = int(input("Enter number: "))
print(f"Factorial of {number} is {Factorial(number)}")
