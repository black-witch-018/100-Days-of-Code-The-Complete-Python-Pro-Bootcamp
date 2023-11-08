# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
true_count = 0
love_count = 0
name1 = name1.lower()
name2 = name2.lower()
true_count += name1.count('t') + name2.count('t')
true_count += name1.count('r') + name2.count('r')
true_count += name1.count('u') + name2.count('u')
true_count += name1.count('e') + name2.count('e')

love_count += name1.count('l') + name2.count('l')
love_count += name1.count('o') + name2.count('o')
love_count += name1.count('v') + name2.count('v')
love_count += name1.count('e') + name2.count('e')

love_score = true_count*10 + love_count

if love_score < 10 or love_score > 90:
  print(f"Your score is {love_score}, you go together like coke and mentos.")
elif love_score >= 40 and love_score <= 50:
  print(f"Your score is {love_score}, you are alright together.")
else:
  print(f"Your score is {love_score}.")