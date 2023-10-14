import random
while True:
    my_answer = input("Choose: Rock, Paper or Scissors: ")
    my_answer = my_answer.lower()
    if my_answer != "rock" and  my_answer != "paper" and my_answer != "scissor":
        print("Please chose a correct answer")
        continue

    computer_answer = random.choice(["rock", "paper", "scissor"])
    print(f"Computer choose: {computer_answer}")
    if my_answer == computer_answer:
        print("You tied")
        continue
    elif my_answer == "paper" and computer_answer == "rock":
        print("You Win")
        break
    elif my_answer == "rock" and computer_answer == "scissor":
        print("You Win")
        break
    elif my_answer == "scissor" and computer_answer == "paper":
        print("You Win")
        break
    else:
        print("You lose, Try again")
