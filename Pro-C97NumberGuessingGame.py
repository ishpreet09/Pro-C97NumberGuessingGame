import random

print("Number Guessing Game")
print("Guessn a number(0 to 9)")

number= random.randint(0,9)
chances=0

while chances < 5:
   guess=int(input("Enter your guess:- "))

   if guess==number:
       print("Congrats!! You won the game")
       break

   elif guess > number:
           print("You are too high. Think of lower than", guess)

   else:
           print("You are too low. Think of above than", guess)
   chances+=1     

if not chances>5 and guess != number:
    print("You lost the game. The number is", number)

