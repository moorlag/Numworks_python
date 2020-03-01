import random 

#returns a number
def roll_dice():
  print (random.randint(1, 6)) 

print("""
This python script returns a random value between 1 and 6. It's a dice
""")

flag = True
while flag:
   user_prompt = input(">")
   if user_prompt.lower() == "quit":
      flag = False
   else:
     print("Rolling dice...\nYour number is:") 
     roll_dice()
