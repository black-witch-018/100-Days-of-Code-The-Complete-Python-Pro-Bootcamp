
# First Logic

#Write your code below this row 👇
flag = True
for i in range(1,101):
  flag = True
  if i%3 == 0:
    print("Fizz", end="")
    flag = False
  if i%5 == 0:
    print("Buzz", end="")
  elif flag:
    print(i,end="")
  print()