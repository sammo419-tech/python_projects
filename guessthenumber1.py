import random

num = random.randint(1,10)
print(num)

while True:
    user_input = int(input("Pick a number between 1 and 10: "))
    if num == user_input:
        print("You guessed correctly")
        break
    elif user_input != num:
        print("You did not guess correctly")

