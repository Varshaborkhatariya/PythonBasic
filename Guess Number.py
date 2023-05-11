import random

num=random.randint(1,30)

while True:
    guess=int(input("Guess A Number Between 1 to 30:"))
    if guess==num:
       print("You Guess A Correct Number")
       break
    elif guess>num:        
       print("You Guess A Greter Number")
    elif guess<num:
       print("You Guess A Smaller Number")
       
