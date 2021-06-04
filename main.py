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
rps = int(input("What do you choose? Type 0 for Rock, 1 for Paper and 2 for Scissors.\n")) 
listrps = [rock, paper, scissors]
random = random.choice(listrps)

if rps == 0:
  print(rock)
  if random == scissors:
    print(f"Computer chose:\n{scissors}\nYou win.")
  elif random == rock:
    print(f"Computer chose:\n{rock}\nIt is a draw. Let's play again!")
  elif random == paper:
    print("You lose")
elif random == paper:
    print("You lose")

if rps == 1:
  print(paper)
  if random == rock:
    print(f"Computer chose:\n{rock}\nYou win.")
  elif random == paper:
    print(f"Computer chose:\n{paper}\nIt is a draw. Let's play again!")
  elif random == scissors:
    print("You lose")
elif random == scissors:
    print("You lose")

if rps == 2:
  print(scissors)
  if random == paper:
    print(f"Computer chose:\n{paper}\nYou win.")
  elif random == scissors:
    print(f"Computer chose:\n{scissors}\nIt is a draw. Let's play again!")
  elif random == rock:
    print("You lose")
else:
  print("You lose")