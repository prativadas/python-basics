import random                                       # because you want one player(here computer) to choose randomly, so that other player wont know

# Snake Water Gun or Rock Paper Scissors
def gameWin(comp, you):                                # if both player choose same option, its a tie.
    # If two values are equal, declare a tie!
    if comp == you:
        return None

    # Check for all possibilities when computer chose s
    elif comp == 's':                   # s=nake, w=water, g=gun
        if you=='w':
            return False                # false = you loose, true= you win
        elif you=='g':
            return True                
    
    # Check for all possibilities when computer chose w
    elif comp == 'w':
        if you=='g':
            return False
        elif you=='s':
            return True
    
    # Check for all possibilities when computer chose g
    elif comp == 'g':
        if you=='s':
            return False
        elif you=='w':
            return True

randNo = random.randint(1, 3)             #random is a python module that has a builtin function randint(). produces random int b/w the range
if randNo == 1:
    comp = 's'
elif randNo == 2:
    comp = 'w'
elif randNo == 3:
    comp = 'g'

you = input("Your Turn: Snake(s) Water(w) or Gun(g)?")

print(f"You chose {you}")                                  #print what you choose


print("Comp Turn: Snake(s) Water(w) or Gun(g)?")        

print(f"Computer chose {comp}")        #never print this before. you choose your option. because tie happens or you win always after seeing ehat comp chooses.
                                       #f string lets you choose variable in curly brace{}. prints what comp chooses.

a = gameWin(comp, you)                                    # called function game() and strored result in a.


            

if a == None:
    print("The game is a tie!")
elif a:
    print("You Win!")
else:
    print("You Lose!")