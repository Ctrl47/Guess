
#Guess The Number
#Guess the number from 1 to 100


from random import randint

number = randint(1, 100)

guess = None
score = 0
while number != guess:
    guess = int(input("Guess The Number! "))

    if guess == number:
        print(f"You guessed! Your score: {score}")
    elif guess < number:
        print("Your guess is too low try next time \n")
    elif guess > number:
        print("Your guess is too high try next time \n")
