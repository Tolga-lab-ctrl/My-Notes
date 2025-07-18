height = int(input("What is you height?: "))
credit = int(input("How many credit do you have?: "))

if height >= 137 and credit >= 10:
  print("Enjoy the ride!")
elif height < 137 and credit >= 10:
  print("You are not tall enough to ride.")
elif height >= 137 and credit < 10:
  print("You are so Broke :)")
else:
  print("Not met either requirements")
