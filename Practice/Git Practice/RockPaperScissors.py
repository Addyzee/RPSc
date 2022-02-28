# Write your solution below the starter code
# Follow the instructions in the tab to the right

import random
from time import sleep

# Welcome the user to the game
print("Welcome to rock, paper, scissors. Let's play. First to win three games wins!")
play_game=0
computer_win=0
user_win=0
while play_game<3:

# Make a choice for the computer player
 R="Rock"
 P="Paper"
 S="Scissors"
 RPS=[R, P, S]
 computer_play=random.choice(RPS)
# Get a choice from the user
 print(f"You have won {user_win} times and the computer has won {computer_win} times")
 user_play=input("Rock, Paper or Scissors? ").title()
# Compare the user and computer choice
 if not (user_play == R or user_play == P or user_play == S):
     print("Invalid choice.")
 if computer_play==user_play:
  print(f"Computer chooses {computer_play}")
  print("PROCESSING")
  sleep(1)
  print(".")
  sleep(1)
  print(".")
  sleep(1)
  print(".")
  print(f"{computer_play} and {user_play}. It's a draw.")
 elif user_play== R:
  print(f"Computer chooses {computer_play}")
  print("PROCESSING")
  sleep(1)
  print(".")
  sleep(1)
  print(".")
  sleep(1)
  print(".")
  if computer_play== S:
      print(f"{R} crashes {S}. You win!")
      user_win+=1
  else:
      print(f"{P} covers {R}. Computer wins!")
      computer_win+=1
 elif user_play== S:
  print(f"Computer chooses {computer_play}")
  print("PROCESSING")
  sleep(1)
  print(".")
  sleep(1)
  print(".")
  sleep(1)
  print(".")
  if computer_play== P:
      print(f"{S} cuts {P}. You win!")
      user_win+=1
  else:
      print(f"{R} crashes {S}. Computer wins!")
      computer_win+=1
 elif user_play==P:
  print(f"Computer chooses {computer_play}")
  print("PROCESSING")
  sleep(1)
  print(".")
  sleep(1)
  print(".")
  sleep(1)
  print(".")
  if computer_play== R:
      print(f"{P} covers {R}. You win!")
      user_win+=1
  else:
      print(f"{S} cuts {P}. Computer wins!")
      computer_win+=1
 
 if computer_win>user_win:
     play_game=computer_win
 else:
     play_game=user_win
if computer_win==3:
     print("Nice work to the Computer. He was the first to win 3 times")
     print("Better luck next time")
else:
    print("Nice work. You were the first to win 3 times!")
exit(0)
