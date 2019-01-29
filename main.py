# Importing Modules..
from tkinter import *
from time import sleep
import random

# Seeding Random so that same number is not taken repeatedly....
random.seed()

#Global Variables
global POS
global b
global bo2
global bo3
bo3 = True
global TURN
global DIFF
DIFF = []
global POS_LEFT
POS_LEFT = [1,2,3,4,5,6,7,8,9]
global COM_POS_SEL
COM_POS_SEL = []
global USER_POS_SEL
USER_POS_SEL = []
global COM_POS_PRIO
COM_POS_PRIO = [1,3,7,9]
global TEMP
TEMP = {}
global b
b = True
ch = input("Do you want to Play?(Y/N)[Say Y if you are scared of me.....]\n")
if(ch == 'Y'):
    TURN = 1
else:
    TURN = 0
# USER's TURN....
def myturn(event):
    global POS,POS_LEFT,COM_POS_PRIO,bo3
    bo3 = True
    if event.x >= 120 and event.x < 240 and event.y >= 40 and event.y < 140:
        POS = 1
        my_canvas.create_text(180, 90, font = ("Callibri",20), text = 'X')
    elif  event.x >= 240 and event.x < 360 and event.y >= 40 and event.y < 140:
        POS = 2
        my_canvas.create_text(300, 90, font = ("Callibri",20), text = 'X')
    elif  event.x >= 360 and event.x < 480 and event.y >= 40 and event.y < 140:
        POS = 3
        my_canvas.create_text(420, 90, font = ("Callibri",20), text = 'X')
    elif  event.x >= 120 and event.x < 240 and event.y >= 140 and event.y < 240:
        POS = 4
        my_canvas.create_text(180, 200, font = ("Callibri",20), text = 'X')
    elif  event.x >= 240 and event.x < 360 and event.y >= 140 and event.y < 240:
        POS = 5
        my_canvas.create_text(300, 200, font = ("Callibri",20), text = 'X')
    elif  event.x >= 360 and event.x < 480 and event.y >= 140 and event.y < 240:
        POS = 6
        my_canvas.create_text(420, 200, font = ("Callibri",20), text = 'X')
    elif  event.x >= 120 and event.x < 240 and event.y >= 240 and event.y < 340:
        POS = 7
        my_canvas.create_text(180, 310, font = ("Callibri",20), text = 'X')
    elif  event.x >= 240 and event.x < 360 and event.y >= 240 and event.y < 340:
        POS = 8
        my_canvas.create_text(300, 310, font = ("Callibri",20), text = 'X')
    elif  event.x >= 360 and event.x < 480 and event.y >= 240 and event.y < 340:
        POS = 9
        my_canvas.create_text(420, 310, font = ("Callibri",20), text = 'X')
    else:
        print("CLICK ON APPROPRIATE POSITION.")
        POS = -1
    if POS!=-1:
        change()
        POS_LEFT.remove(POS)
        if POS in COM_POS_PRIO:
            COM_POS_PRIO.remove(POS)
        USER_POS_SEL.append(POS)
    i = 0
    while i < len(USER_POS_SEL)-1:
        j = i + 1
        while j < len(USER_POS_SEL):
            if checkrow([USER_POS_SEL[i],USER_POS_SEL[j],POS]) or checkcol([USER_POS_SEL[i],USER_POS_SEL[j],POS]) or checkdiog([USER_POS_SEL[i],USER_POS_SEL[j],POS]):
                bo3 = False
                break
            j = j + 1
        i = i + 1
        if not bo3:
            break
    

# Change TURN....
def change():
    global TURN
    TURN = 0

def checkrow(l):
    if((1 in l and 2 in l and 3 in l) or (4 in l and 5 in l and 6 in l) or (7 in l and 8 in l and 9 in l)):
        return True
    return False

def checkcol(l):
    if((1 in l and 4 in l and 7 in l) or (2 in l and 5 in l and 8 in l) or (3 in l and 6 in l and 9 in l)):
        return True
    return False

def checkdiog(l):
    if((1 in l and 5 in l and 9 in l) or (3 in l and 5 in l and 7 in l)):
        return True
    return False

# COM's TURN....
def comturn():
    global TURN,POS,COM_POS_PRIO,COM_POS_SEL,b,USER_POS_SEL,POS_LEFT,bo2
    bo = True
    bo2 = True
    # AI Algorithm
    for x in POS_LEFT:
                i = 0
                while i < len(USER_POS_SEL)-1:
                    j = i + 1
                    while j < len(USER_POS_SEL):
                        if checkrow([USER_POS_SEL[i],USER_POS_SEL[j],x]) or checkcol([USER_POS_SEL[i],USER_POS_SEL[j],x]) or checkdiog([USER_POS_SEL[i],USER_POS_SEL[j],x]):
                            POS = x
                            bo2 = False
                            break
                        j = j + 1
                    i = i + 1
                    if not bo2:
                        break
                if not bo2:
                    break
    if len(COM_POS_PRIO)>0 and len(COM_POS_SEL)<2 and bo2:
        POS = random.choice(COM_POS_PRIO)
        COM_POS_PRIO.remove(POS)
    else:
        for x in POS_LEFT:
            i = 0
            while i < len(COM_POS_SEL)-1:
                j = i + 1
                while j < len(COM_POS_SEL):
                    if checkrow([COM_POS_SEL[i],COM_POS_SEL[j],x]) or checkcol([COM_POS_SEL[i],COM_POS_SEL[j],x]) or checkdiog([COM_POS_SEL[i],COM_POS_SEL[j],x]):
                        POS = x
                        b = False
                        break
                    j = j + 1
                i = i + 1
                if not b:
                    break
            if not b:
                break
        else:
            for x in POS_LEFT:
                i = 0
                while i < len(USER_POS_SEL)-1:
                    j = i + 1
                    while j < len(USER_POS_SEL):
                        if checkrow([USER_POS_SEL[i],USER_POS_SEL[j],x]) or checkcol([USER_POS_SEL[i],USER_POS_SEL[j],x]) or checkdiog([USER_POS_SEL[i],USER_POS_SEL[j],x]):
                            POS = x
                            bo = False
                            break
                        j = j + 1
                    i = i + 1
                    if not bo:
                        break
                if not bo:
                    break
                if bo:
                    POS = random.choice(POS_LEFT)
        
    
    if POS == 1:
        my_canvas.create_text(180, 90, font = ("Callibri",20), text = 'O')
    elif POS == 2:
        my_canvas.create_text(300, 90, font = ("Callibri",20), text = 'O')
    elif POS == 3:
        my_canvas.create_text(420, 90, font = ("Callibri",20), text = 'O')    
    elif POS == 4:
        my_canvas.create_text(180, 200, font = ("Callibri",20), text = 'O')
    elif POS == 5:
        my_canvas.create_text(300, 200, font = ("Callibri",20), text = 'O')
    elif POS == 6:
        my_canvas.create_text(420, 200, font = ("Callibri",20), text = 'O')
    elif POS == 7:
        my_canvas.create_text(180, 310, font = ("Callibri",20), text = 'O')
    elif POS == 8:
        my_canvas.create_text(300, 310, font = ("Callibri",20), text = 'O')
    else:
        my_canvas.create_text(420, 310, font = ("Callibri",20), text = 'O')
    TURN = 1
    COM_POS_SEL.append(POS)
    POS_LEFT.remove(POS)
    sleep(0.5)


# Main()
root = Tk()
root.title("TicTacToe")
# Initiating Canvas...
my_canvas = Canvas(root, width = 640, height = 480, background = 'white')
my_canvas.pack()
root.bind("<Button-1>", myturn)
# Drawing Lines...
# Vertical Lines.....
my_canvas.create_line(240,40,240,360)
my_canvas.create_line(360,40,360,360)
# Horizontal Lines.....
my_canvas.create_line(120,140,480,140)
my_canvas.create_line(120,260,480,260)

# Printing positions...
my_canvas.create_text(230, 130, text = '1')
my_canvas.create_text(350, 130, text = '2')
my_canvas.create_text(470, 130, text = '3')
my_canvas.create_text(230, 250, text = '4')
my_canvas.create_text(350, 250, text = '5')
my_canvas.create_text(470, 250, text = '6')
my_canvas.create_text(230, 350, text = '7')
my_canvas.create_text(350, 350, text = '8')
my_canvas.create_text(470, 350, text = '9')

# Instructions
my_canvas.create_text(610,15, text = 'YOU - X')
my_canvas.create_text(610,30, text = 'COM - O')
my_canvas.create_text(300,15, text = 'CLICK TO PLACE')

# MainLoop
while True:
    if(TURN == 1):
        if(len(POS_LEFT) == 0):
            print('GameOver! DRAW. NICE Gameplay.')
            # my_canvas.create_text(240, 440, text = 'GameOver! DRAW. NICE Gameplay.....')
            sleep(2)
            root.destroy()
            break
        elif(not b):
            print('GameOver! I WON the Game.:)')
            # my_canvas.create_text(240, 440, text = 'GameOver! Computer WON the Game.')
            sleep(2)
            root.destroy()
            break



    else:
        if(len(POS_LEFT) == 0 and b):
            print('GameOver! DRAW. NICE Gameplay.')
            # my_canvas.create_text(240, 440, text = 'GameOver! DRAW. NICE Gameplay.....')
            sleep(2)
            root.destroy()
            break
        elif(not b):
            print('GameOver! I WON the Game.:)')
            # my_canvas.create_text(240, 440, text = 'GameOver! Computer WON the Game.')
            sleep(2)
            root.destroy()
            break
        if(not bo3):
            print('GameOver! You Won The game with the only strategy Possible.:(')
            sleep(2)
            root.destroy()
            break
        else:
            comturn() 
    root.update()       
root.mainloop()