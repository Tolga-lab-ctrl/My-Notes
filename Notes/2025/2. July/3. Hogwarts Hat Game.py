print("Hogwarts Hat Game, I Had Good Time While Making This.")
print("Made by TheLagSquad(TISSEC)")
print("----------------------------------------------------")
Slytherin = 0
Ravenclaw = 0
Hufflepuff = 0
Gryffindor = 0
print("Q1) Do you like Dawn or Dusk?")
print("  1) Dawn")
print("  2) Dusk")
print("----------------------------------------------------")
QDuskDawn = int(input("Answer with 1 or 2: "))
if QDuskDawn == 1:
  Gryffindor = Gryffindor + 1
  Ravenclaw = Ravenclaw + 1
elif QDuskDawn == 2:
  Hufflepuff = Hufflepuff + 1
  Slytherin = Slytherin + 1
else:
  print("Wrong Input")
print("----------------------------------------------------")
print("Q2) When I’m dead, I want people to remember me as:")
print("  1) The Good")
print("  2) The Great")
print("  3) The Wise")
print("  4) The Bold")
print("----------------------------------------------------")
Q2 = int(input("Answer with 1-4: "))
if Q2 == 1:
  Hufflepuff = Hufflepuff + 2
elif Q2 == 2:
  Slytherin = Slytherin + 2
elif Q2 == 3:
  Ravenclaw = Ravenclaw + 2
elif Q2 == 4:
  Gryffindor = Gryffindor + 2
else:
  print("Wrong Input")
print("----------------------------------------------------")
print("Q3) Which kind of instrument most pleases your ear?")
print("  1) The violin")
print("  2) The trumpet")
print("  3) The piano")
print("  4) The drum")
print("----------------------------------------------------")
Q3 = int(input("Answer with 1-4: "))
if Q3 == 1:
  Slytherin = Slytherin + 4
elif Q3 == 2:
  Hufflepuff = Hufflepuff + 4
elif Q3 == 3:
  Ravenclaw = Ravenclaw + 4
elif Q3 == 4:
  Gryffindor = Gryffindor + 4
else:
  print("Wrong Input")
print("----------------------------------------------------")
print(f"Score for 🦁 Gryffindor: {Gryffindor}")
print(f"Score for 🦅 Ravenclaw: {Ravenclaw}")
print(f"Score for 🦡 Hufflepuff: {Hufflepuff}")
print(f"Score for 🐍 Slytherin: {Slytherin}")
print("----------------------------------------------------")
if Gryffindor > Ravenclaw and Gryffindor > Hufflepuff and Gryffindor > Slytherin:
  print(f'You are in house:🦁 Gryffindor')
elif Ravenclaw > Gryffindor and Ravenclaw > Hufflepuff and Ravenclaw > Slytherin:
  print(f'You are in house:🦅 Ravenclaw')
elif Hufflepuff > Gryffindor and Hufflepuff > Ravenclaw and Hufflepuff > Slytherin:
  print(f'You are in house:🦡 Hufflepuff')
elif Slytherin > Gryffindor and Slytherin > Ravenclaw and Slytherin > Hufflepuff:
  print(f'You are in house:🐍 Slytherin')
else:
  print("Something Went Wrong")
