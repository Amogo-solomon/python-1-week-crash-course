secret_number = 7

while True:
    guess = int(input("Guess the number (1-10): "))

    if guess == secret_number:
        print("You guessed it!")
        break
    else:
        print("Wrong guess, try again!")