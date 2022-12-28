import random

user_input = int(input("Enter a number between 1 and 10: "))
count = 0

while True:
    guess = random.randint(1,10)
    if guess == user_input and count == 0:
        print(f"The computer guessed your number first try")
        break
    elif guess == user_input:
        print(f"The computer guessed your number in {count} attempts")
        break
    elif guess != user_input:
        count = count + 1
