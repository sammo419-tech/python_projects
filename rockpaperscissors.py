import random

mylist = ["rock", "paper", "scissor"]
computer = 0
player = 0

for i in range(3):
    user_input = input("Enter rock, paper, or scissor: ")
    computer_pick = random.choice(mylist)
    if computer_pick == user_input:
        print("Tie")
    elif computer_pick == "rock" and user_input == "scissor":
        print("Computer point")
        computer = computer + 1
    elif computer_pick == "scissor" and user_input == "rock":
        print("Player point")
        player = player + 1
    elif computer_pick == "scissor" and user_input == "paper":
        print("Computer point")
        computer = computer + 1
    elif computer_pick == "paper" and user_input == "scissor":
        print("Player point")
        player = player + 1
    elif computer_pick == "paper" and user_input == "rock":
        print("Computer point")
        computer = computer + 1
    elif computer_pick == "rock" and user_input == "paper":
        print("Player point")
        player = player + 1

# print(player)
# print(computer)

if player > computer:
    print("Player wins!")
elif computer > player:
    print("Player wins!")
elif computer == player:
    print("Tie game")
        

    
    