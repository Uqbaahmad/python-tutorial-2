def add(a, b):
    print(f"ADDING {a} + {b}")
    return a + b

def subtract(a, b):
    print(f"SUBTRACT {a} - {b}")
    return a - b

def multiply(a, b):
    print(f"MULTIPLY {a} * {b}")
    return a * b

def divide(a, b):
    print(f"DIVIDE {a} / {b}")
    return a / b

print("Let's do some math with the function")

a = int(input("A:"))
b = int(input("B:"))
age = add(a, b)
height = subtract(10 , 4.6)
weight = multiply(5, 10)
iq = divide(200, 2)

print(f"age: {age}, height: {height}, weight: {weight}, iq: {iq}")

# A puzzle for the extra credit, type it in anyway.

print("Here is a puzzle")

what = add(age, subtract(height, multiply(weight, divide(iq, 2))))

print("That becomes: ", what , ". Can you do it by hand")
