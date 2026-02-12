# exception handling
#programs should not crash
#Handle errors gracefully

try:
    number = int(input("Enter a number "))
    print("You entered: ", number)
except ValueError:
    print("Invalid input! Please enter a valid number.")
finally:
    print("Program finished.")


