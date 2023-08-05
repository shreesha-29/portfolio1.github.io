import random
def play():
    user =input("___Welcome to rock,paper,scissor game___\n please let me know your choice!\n Your Options are 'r' for rock,'p' for paper and 's' for scissor-- ").lower()
    computer = random.choice(['r','p','s'])

    if user==computer:
        return "Oh! It's a tie"
    
    if is_run(user,computer):
        return "You won!!!"
    
    return "Your lost!!"
def is_run(player,opponent):
    if (player=='r' and opponent=="s") or (player=='p' and opponent=="r") or(player=='s' and opponent=="p"):
        return True
print(play())