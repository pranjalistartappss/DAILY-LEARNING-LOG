secret_number = 25
chances = 5

while chances > 0:
    guess = int(input("Guess the Number: "))

    if guess == secret_number:
        print("Congratulations! You guessed correctly.")
        break

    elif guess < secret_number:
        print("Higher Number Please")

    else:
        print("Lower Number Please")

    chances -= 1
    print("Remaining Chances:", chances)

if chances == 0:
    print("Game Over")
    print("The Secret Number was:", secret_number)