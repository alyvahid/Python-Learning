# using print ()
from datetime import date, datetime
import keyword

print("Hello Alisha")

# Using type() function
print(type("Hello Alisha"))
a = 10
print(type(a))

# Using input() function
c = input("Enter your name: ")
print("Hello " + c)
# print("Hello ", c) can be write like this

# Using datetime() function
now = datetime.now()
print("Now:", now)  # Output: 2026-08-18 16:51:00.123456

# Get just today's date
today = date.today()
print("Today's Date:", today)

help("keywords")  # Output: Help on module keyword