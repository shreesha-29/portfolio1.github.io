import random
print("welcome")
x = int(input('Please tell me the range of numbers in which you want to play starting from 1:'))
random_number=random.randint(1,x)
c=0
def guess(x):
   c=1
   guess=1
   while guess!=random_number:
     print("\n")
     print("Attempt number--")
     print(c)
     guess=int(input(f"Please guess a number between 1 and {x}--"))
     if guess<random_number:
       print("The number guessed is less than actual number")
       c=c+1
     elif guess>random_number: 
        print("The number guessed is more than actual number")
        c=c+1 
guess(x)
print(f"Yes!! You are right.You have guessed the right number that is {random_number}. ")    


 