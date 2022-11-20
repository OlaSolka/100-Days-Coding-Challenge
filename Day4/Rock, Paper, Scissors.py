rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
import random
print("Welcome to the \"Rock, paper scissors\"!\n What do you choose?")
choice = int(input("Type 0 for Rock, 1 for Paper or 2 for Scissors: "))
if choice == 0:
    print(rock)
elif choice == 1:
    print(paper)
elif choice == 2:
    print(scissors)
else:
    print("Unknown Value")

print("Computer chose: ")

computer_choice_list = [0, 1, 2]
for i in range(1):
    computer_choice = random.choice(computer_choice_list)
if computer_choice == 0:
    print(rock)
elif computer_choice == 1:
    print(paper)
elif computer_choice == 2:
    print(scissors)

if choice==computer_choice:
    print("It's a draw!")
elif choice == 0 and computer_choice == 1:
    print("Computer wins!")
elif choice == 0 and computer_choice == 2:
    print("You win!")
elif choice == 1 and computer_choice == 0:
    print("You win!")
elif choice == 1 and computer_choice == 2:
    print("Computer wins!")
elif choice == 2 and computer_choice == 0:
    print("Computer wins!")
elif choice == 2 and computer_choice == 1:
    print("You win!")
else:
    print("Something went wrong!")


