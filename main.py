# Importing Modules..
from tkinter import *
from time import sleep
import random

# Seeding Random so that same number is not taken repeatedly....
random.seed()

#Global Variables
global POS
global TURN
TURN = 0
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
b = True

# USER's TURN....
def myturn(event):
    # print("clicked at ", event.x, event.y)
    global POS,POS_LEFT,COM_POS_PRIO
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
        print(POS_LEFT)
        if POS in COM_POS_PRIO:
            COM_POS_PRIO.remove(POS)
        USER_POS_SEL.append(POS)
    print(POS)

# Change TURN....
def change():
    global TURN
    TURN = 0

# COM's TURN....
def comturn():
    global TURN,POS,COM_POS_PRIO,COM_POS_SEL,b,USER_POS_SEL
    # AI Algorithm
    if len(COM_POS_PRIO) > 2 or len(COM_POS_SEL)<=1:
        POS = random.choice(COM_POS_PRIO)
        COM_POS_PRIO.remove(POS)
    else:
        for x in POS_LEFT:
            i = 0
            while i < len(COM_POS_SEL)-1:
                if abs(x - COM_POS_SEL[i]) == abs(x - COM_POS_SEL[i+1]) or abs(COM_POS_SEL[i] - COM_POS_SEL[i+1]) == abs(x - COM_POS_SEL[i+1]):
                    POS = x
                    b = False
                    break
                i = i + 1
            if not b:
                break
        else:
            POS = random.choice(POS_LEFT)
    '''if len(USER_POS_SEL) >=2:
        for x in POS_LEFT:
            if abs(x - USER_POS_SEL[0]) == abs(x - USER_POS_SEL[1]) or abs(USER_POS_SEL[0] - USER_POS_SEL[1]) == abs(x - USER_POS_SEL[1]):
                POS = x
                break'''

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
    print(POS_LEFT, COM_POS_SEL)
    sleep(0.5)


# Main()
root = Tk()
# Initiating Canvas...
my_canvas = Canvas(root, width = 640, height = 480, background = 'white')
my_canvas.pack()
root.bind("<Button-1>", myturn)
TXT = my_canvas.create_text(40, 15, text = 'MY TURN')
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
        my_canvas.itemconfigure(TXT, text = "YOUR TURN")
        if(len(POS_LEFT) == 0):
            print('GameOver! DRAW. NICE Gameplay.....')
            root.destroy()
            break
    else:
        my_canvas.itemconfigure(TXT, text = "MY TURN")
        if(len(POS_LEFT) == 0 and b):
            print('GameOver! DRAW. NICE Gameplay.....')
            root.destroy()
            break
        elif(not b):
            print('GameOver! Computer WON the Game.')
            root.destroy()
            break
        else:
            comturn()
    root.update()
        
        
root.mainloop()