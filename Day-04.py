import random

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
game_images = [rock, paper, scissors]
user=int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors: "))
print(game_images[user])
computer=random.randint(0,2)
print("computer chose:")
print(game_images[computer])
if user==0 and computer==1:
    print("computer wins!")
elif user==0 and computer==2:
    print("user wins!")
elif user==1 and computer==0:
    print("user wins!")
elif user==1 and computer==2:
    print("computer wins!")
elif user==2 and computer==0:
    print("computer wins!")
elif user==2 and computer==1:
    print("user wins!")
elif user == computer:
    print("Draw!")