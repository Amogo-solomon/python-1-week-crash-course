# scope
x = 10 # global variable

def show_number():
    x = 5 # local variable
    print("Inside function:", x)

show_number()
print("Outside function:", x)

#Local variables exist only inside function
# Global variables exist outside