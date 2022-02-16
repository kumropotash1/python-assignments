# Write a program that displays ‘True’ if a number is even and ‘False’ otherwise based upon the accepted non-zero input from the user.
def is_even(num):
  if(num % 2):
    print(False)
  else:
    print(True)


ip = (int)(input("enter a number:"))

is_even(ip)
