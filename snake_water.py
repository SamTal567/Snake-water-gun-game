import random
# Snake Water Gun or Rock Paper Scissors
def game(comp,you):
    # if 2 values are equal than declare a tie
    if comp == you:
        return None
    #check for possibilities when comp chooses s
    elif comp =='s':
        if you == 'w':
            return False
        elif you == 'g':
            return True
        #check for possibilities when comp chooses w
    elif comp =='w':
        if you == 'g':
            return False
        elif you == 's':
            return True
        #check for possibilities when comp chooses g
    elif comp =='g':
        if you == 's':
            return False
        elif you == 'w':
            return True


print("Comp turn: Snake(s) Water(w) or Gun(g)")
randNo = random.randint(1,3)
if randNo == 1:
    comp = 's'
elif randNo == 2:
    comp = 'w'
elif randNo == 3:
    comp = 'g'
you = input("your turn: Snake(s) Water(w) or Gun(g)")

a = game(comp,you)
print(f"computer chose {comp}")
print(f"you chose {you} ")

if a== None:
    print("the game is a tie!")
elif a:
    print("you win!")
else:
    print("you lose")