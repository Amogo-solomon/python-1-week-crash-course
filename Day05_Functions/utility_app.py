#create functions for:
# checking if number is even
# Calculating square
#Converting Celcius to Fahrenheit

def is_even(number):
    return number % 2 == 0

def square(number):
    return number * number

def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32

def main():
    print("=== Utility App ===")
    print("1. Check if number is even")
    print("2. Calculate square of a number")
    print("3. convert celsius to Fahrenheit")

    choice = input("Choose an option (1-3): ")

    if choice == "1":
        num = int(input("Enter a number: "))
        if is_even(num):
            print("The number is even.")
        else:
            print("The number is odd.")

    elif choice ==  "2":
        num = int(input("Enter a number: "))
        print("Square is:", square(num))

    elif choice == "3":
        c = float(input("Enter temperature in Celcius: "))
        print("Fahrenheight: ", celsius_to_fahrenheit(c))

    else:
        print("Invalid choice!")

if __name__ == "__main__":
    main()