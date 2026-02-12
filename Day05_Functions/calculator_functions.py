# return values
#retun sends data back
# Functions should return values, not just print

def add(a, b):
    return a + b

def substract(a, b):
    return a - b

x = int(input("Enter first number: "))
y = int(input("Enter second number: "))

print("Sum:", add(x, y))
print("Difference:", substract(x, y))

