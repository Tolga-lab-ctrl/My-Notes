import random

one = 'Yes - definitely.'
two = 'It is decidedly so.'
three = 'Without a doubt.'
four = 'Reply hazy, try again.'
five = 'Ask again later.'
six = 'Better not tell you now.'
seven = 'My sources say no.'
eight = 'Outlook not so good.'
nine = 'Very doubtful.'

num = random.randint(1, 9)
question = input("Ask a question: ")

if num == 1:
  print(one)
elif num == 2:
  print(two)
elif num == 3:
  print(three)
elif num == 4:
  print(four)
elif num == 5:
  print(five)
elif num == 6:
  print(six)
elif num == 7:
  print(seven)
elif num == 8:
  print(eight)
elif num == 9:
  print(nine)
