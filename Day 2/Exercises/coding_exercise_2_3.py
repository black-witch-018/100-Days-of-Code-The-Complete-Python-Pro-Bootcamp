# 🚨 Don't change the code below 👇
age = input("What is your current age?")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
max_age = 90
age = int(age)
years_remaining = max_age - age
days_left = years_remaining * 365
weeks_left = years_remaining * 52
months_left = years_remaining * 12
print(f"You have {days_left} days, {weeks_left} weeks, and {months_left} months left.")