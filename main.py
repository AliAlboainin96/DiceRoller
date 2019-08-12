import random
import os
import time



while loop == True:

    # function to clear the console

    def cls():
        os.system('Cls ' if os.name =='nt' else 'clear')

    roles = int(input("How Many Times Do Want To ROll The Dice? "))
 
    # detects if input is 0 or less

    if roles == 0:
        print("0 or below are invalid input!/n")

    # menu ui

    cls()
    print("Rolling...")
    time.sleep(1)
    cls()
   
    if roles == 0:
        print("0 or below are invalid input!/n") 
    
    # function to generate random numbers

    def test():
        for roles_dice in range(roles):    
            random_num = random.randint(1,6)           
        return random_num   
    
    for rolls_num in range(roles):
        rolls_num += 1

        roll_form = rolls_num

        print("Roll {0}: {1}".format(roll_form,test()))
 
    # loop       

    loop = input("\nAgain? Y/N ")

    if loop == "yes" or "YES" or "y" or "Y":
        cls()
        loop == True
    elif loop == "n" or "NO" or "n" or  "N":
        cls()
        loop == False
        break
    else:
        cls()
        print("LOADING...")
        time.sleep(10)
        cls()
        print("Wrong Choise next time follow the rules!")
        break