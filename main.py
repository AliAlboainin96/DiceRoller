import random
import sys

loop = True

while loop == True:

    roles = int(input("How Many Times Do Want To ROll The Dice? "))
     
    for roles_dice in range(roles):
        random_num = random.randint(1,6)
        print(random_num)
    
    repeat = input("Do You Want To Repeat? Y/N ")
    while repeat != "y" or "n":

        print("worng choise please select Y/N")
        if repeat == "y":
           continue
        elif repeat == "n":
           sys.exit
    




