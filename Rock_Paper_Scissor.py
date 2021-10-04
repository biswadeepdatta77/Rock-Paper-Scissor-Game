import random
rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""
scissor = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""
paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""
game = [rock, scissor, paper]
game2= ['rock', 'scissor', 'paper']
computer_hand = random.choice(game2)
print("Welcome to Biswadeep Datta's brand new game Rock Paper Scissor.Rules: Type rock or scissor or paper")
user_hand = input("Enter your turn among rock paper scissor ")
print("You chose:")
if(user_hand=='rock'):
    print(rock)
if(user_hand=='paper'):
    print(paper)

if(user_hand=='scissor'):
    print(scissor)

print("Computer chose: ")

if computer_hand=='rock':

    print(rock)
    if computer_hand==user_hand:
        print("Draw")
    
    
    if user_hand=='paper':
        print("You win")
    if user_hand=='scissor':
        print("You lose")



if computer_hand=='paper':
    print(paper)
    
    
    
    if computer_hand==user_hand:
        print("Draw")
    if user_hand=='scissor':
        print("You win")
    if user_hand=='rock':
        print("You lose")



if computer_hand=='scissor':
    print(scissor)
    if computer_hand==user_hand:
        print("Draw")
    if user_hand=='rock':
        print("You win")
    if user_hand=='paper':
        print("You lose")





