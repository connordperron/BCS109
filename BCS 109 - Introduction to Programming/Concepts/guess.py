import random
number = random.randint(1,25)
numGuesses = 0

print("You have five chances to guess a number between 1 and 25")
while numGuesses < 5:
    print("Guess a number between 1 and 25: ")
    guess = input()
    guess = int(guess)
    numGuesses = numGuesses + 1

    if guess < number:
        print("Your guess is too low!")
        print(f"That was guess number:{numGuesses}")

    if guess > number:
        print("Your guess is too high!")
        print(f"That was guess number:{numGuesses}")

    if guess == number:
        break

    guessesLeft=5-numGuesses
    print(f"You have {guessesLeft} guesses lefft")

if guess == number:
    print(f"You guessed the number in {guessesLeft} guesses")

else:
    print(f"Sorry, you are out of guesses. The number was {number}")
