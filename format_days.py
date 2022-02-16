# Write a program in Python to number of days and convert it into years, month and days.
def format_days(days):
  years = (int)(days / 365)
  days = days % 365

  months = (int)(days / 30)
  days = days % 30

  result = ""

  if(years == 1):
    result += f"{years}  year, "
  else:
    result += f"{years}  years, "

  if(months == 1):
    result += f"{months}  month, "
  else:
    result += f"{months}  months, "

  if(days == 1):
    result += f"{days}  day"
  else:
    result += f"{days}  days"

  print(result)


ip = (int)(input("enter a number:"))

format_days(ip)
