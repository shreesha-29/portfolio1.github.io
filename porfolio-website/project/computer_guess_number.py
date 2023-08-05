import random
x = int(input("Please let me (your computer) know what is the maximum range till where number can be guessed-- "))
def compu_guess(x):
    low=1
    high=x
    guess=random.randint(low,high)
    feedback=''
    while feedback!='c':
        if low!=high:
             guess=random.randint(low,high)
        else:
            guess=low
        feedback=input(f'If my guessnumber-- {guess} is too high then type "h"\n or if it is low then type "l" \n or is it is equal then type "c" \n').lower()
        if feedback=='H' or feedback =='h':
            high=guess-1
        elif feedback=='L' or feedback =='l':
            low=guess+1
    print("oh good u guessed right!!")  

compu_guess(x)  
  

           


