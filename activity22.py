import random
print("Welcome to the Number Guessing Game!")
random_number = random.randint(1, 10)
tries = 0
tuloy = True

while tuloy == True:
    guess = int(input("Guess a number between 1 and 10: "))
    tries += 1
    if guess < random_number:
        print("Too low! Try again.")
        continue
    elif guess > random_number:
        print("Too high! Try again.")
        continue
    elif guess == random_number:
        print(f"Congratulations! You've guessed the number {random_number} in {tries} tries.")
        break