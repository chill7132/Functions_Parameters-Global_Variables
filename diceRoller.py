import random,time
s1 = "- - - - -\n|       |\n|   O   |\n|       |\n- - - - -\n"
s2 = "- - - - -\n| O     |\n|       |\n|     O |\n- - - - -\n"
s3 = "- - - - -\n| O     |\n|   O   |\n|     O |\n- - - - -\n"
s4 = "- - - - -\n| O   O |\n|       |\n| O   O |\n- - - - -\n"
s5 = "- - - - -\n| O   O |\n|   O   |\n| O   O |\n- - - - -\n"
s6 = "- - - - -\n| O   O |\n| O   O |\n| O   O |\n- - - - -\n"

def rollnumber():
    print("rolling.....")
    global roll
    roll = random.randint(1,6)
    print(roll)


def show_dice(roll):
    if roll == 1:
        print(s1)
        rollnumber()
    elif roll == 2:
        print(s2)
        rollnumber()
    elif roll == 3:
        print(s3)
        rollnumber()
    elif roll == 4:
        print(s4)
        rollnumber()
    elif roll == 5:
        print(s5)
        rollnumber()
    elif roll == 6:
        print(s6)
        rollnumber()


def asknumber():
    answer = input("How times would you like to roll the dice>>> ")
    if answer == 1:
        print(roll)
    elif answer == 2:
        print(roll)
        print(roll + 2)
    elif answer == 3:
        print(roll)
        print(roll+3)
        print(roll+1)
        
        
rollnumber()
time.sleep(1)
show_dice(roll)
                 

    rollnumber()
    time.sleep(1)
    show_dice(roll)
