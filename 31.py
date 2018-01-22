'''
Exercise 31 : Karvonen Heart Rate
Create a program that prompts for  your age and your resting heart rate.  Use
the Karvonen formula to determine the target heart rate based on a range of
intensities from 55'%' to 95%.  Generate a table with the results.

Constraints:
Don't hard-code the percentages.  Use a loop to increment the percentages from
55 to 95.
Ensure that the heart rate and age are entered as numbers.

Don't allow the user to continue without entering valid inputs.
Display the resuls in a tabular format.
'''

def greeting():
  print("Welcome to Exercise 31: Karvonen Heart Rate")
  print("\n")
  
def age_input():
  age_raw = input("Age:  ")
  if age_raw.isnumeric():
    age = int(age_raw)
    return age
  else:
    print("Must enter a number.")
    age_input()

def pulse_input():
  pulse_raw = input("Resting Pulse:  ")
  if pulse_raw.isnumeric():
    pulse = int(pulse_raw)
    return pulse
  else:
    print("Must enter a number.")
    pulse_input()
    
def table_creation():
  table_i = "Intensity  "
  table_rate = " Rate  "
  table_line = "|"
  intensity = 55
  age = 22
  pulse = 65
  print(table_i, end='')
  print(table_line, end='')
  print(table_rate)
  for character in table_i:
    print("-", end='')
  for character in table_line:
    print("|", end='')
  for character in table_rate:
    print("-", end='')
  print("\n")
  
  
  while intensity < 100:
    TargetHeartRate = (((220 - age) - pulse) * (intensity / 100)) + pulse
    print("{}%".format(intensity), end='')
    for character in table_i[(len(str(intensity))+1):]:
      print(' ', end='')
    print("|", end='')
    print(" {} bpm".format(TargetHeartRate))
    intensity += 5

def main():
    greeting()
    table_creation()
    
main()
