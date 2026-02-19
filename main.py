import random

print("Let's play rock, paper, scissors! You can go first")
user_input = input("Enter rock, paper, or scissors. Make sure to spell it in lowercase")
computer_input = random.randint(1, 3)

if computer_input == 1:
    computer_input = "rock"
if computer_input == 2:
    computer_input = "paper"
if computer_input == 3:
    computer_input = "scissors"

if computer_input == "rock" and user_input == "paper":
    print("I chose " + computer_input + " and you chose " + user_input + ", so you win!")
if computer_input == "paper" and user_input == "scissors":
    print("I chose " + computer_input + " and you chose " + user_input + ", so you win!")
if computer_input == "scissors" and user_input == "rock":
    print("I chose " + computer_input + " and you chose " + user_input + ", so you win!")
if computer_input == "rock" and user_input == "scissors":
    print("I chose " + computer_input + " and you chose " + user_input + ", so I win!")
if computer_input == "paper" and user_input == "rock":
    print("I chose " + computer_input + " and you chose " + user_input + ", so I win!")