import random


def gameWin(comp, you):

    if comp == you:
        return None

    elif comp== 's':
        if you == 'w':
            return False
        elif you == 'g':
            return True

    elif comp== 'w':
        if you == 's':
            return True
        elif you == 'g':
            return False

    elif comp== 'g':
        if you == 's':
            return False
        elif you == 'w':
            return True


print("computer's turn: snake(s) water(w) and gun(g)?")

randNom = random.randint(1,3)
 
if randNom == 1:
    comp = 's'
elif randNom == 2:
    comp = 'w'
elif randNom == 3:
    comp  = 'g'

you = input("Your turn: snake(s) water(w) and gun(g)?: ")

a = gameWin(comp, you)

print(f"computer chose{comp}")
print(f"you chose{you}")

if a == None:
    print("The game is tie.")

elif a:
    print("You won!")
else:
    print("you lose")