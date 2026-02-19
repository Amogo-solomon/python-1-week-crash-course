#Lambda Functions

square = lambda x: x * x
print(square(5))

numbers = [1, 2, 3, 4, 5]
squred = list(map(lambda x: x * x, numbers))
print(squred)