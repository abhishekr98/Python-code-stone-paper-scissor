import random

def game(comp, you):
    if comp == you:
        return None
    elif comp == 'st' :
        if you == 'sc' :
            return False
        elif you == 'p' :
            return True
    elif comp == 'p' :
        if you == 'st' :
            return False
        elif you == 'sc' :
            return True
    elif comp == 'sc' :
        if you == 'p' :
            return False
        elif you == 'st' :
            return True

print("comp turn: choose stone(st) paper (p) or scissor(sc)")

randNo = random.randint(1,3)
if randNo == 1:
    comp = 'st'
elif randNo == 2:
    comp = 'p'
elif randNo == 3:
    comp = 'sc'
    
you = input("your turn: choose stone(st) paper (p) or scissor(sc)")

print(f"comp choose {comp}")
print(f"you chose {you}")
a= game(comp, you)
if a == None:
    print("tie")
elif a:
    print("you win")
else:
    print("you lose")