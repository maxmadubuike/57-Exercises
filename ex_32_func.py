import random

def greeting():
  print("Let's play Guess the Number.")

def difficulty_setting():
  setting_raw = input("Pick a difficulty level (1, 2, or 3): ")
  if setting_raw.isnumeric():
    setting = int(setting_raw)
    if setting < 4:
      return setting
    else:
      print("Length Failed")
      difficulty_setting()
  else:
    print("Numeric Failed.")
    difficulty_setting()

def computer_guess(difficulty):
  if difficulty == 1:
    computer_choice = random.randrange(10)
    print("Computer number is: {}".format(computer_choice))
    return computer_choice
  elif difficulty == 2:
    computer_choice = random.randrange(100)
    print("Computer number is: {}".format(computer_choice))
    return computer_choice
  elif difficulty == 3:
    computer_choice = random.randrange(1000)
    print("Computer number is: {}".format(computer_choice))
    return computer_choice
  else:
    print("Invalid difficulty")
