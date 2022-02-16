# Write a program in Python to print the following series using While Loops
# 100, 81, 64, 49, 36, 25, …., 4
def print_squares_descending():
  i = 100
  while i >= 2:
    print(i*i)
    i -= 1


print_squares_descending()
