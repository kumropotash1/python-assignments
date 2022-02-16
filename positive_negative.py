# Write a program in Python to print the words ‘Negative’, ‘Zero’ or ‘Positive’ based upon the input accepted from the user.
def positive_negative(num):
  if(num < 0):
    print("Negative")
  elif(num == 0):
    print("Zero")
  else:
    print("Positive")


ip = (int)(input("enter a number:"))

positive_negative(ip)
