import random
import os
import time

def cls():
    # function to clear the console
        os.system('Cls ' if os.name =='nt' else 'clear')

while True:
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

        print("Roll {0}: {1}".format(roll_form,test())
