# Importing Modules..
from tkinter import *
from time import sleep

global POS
global TRUN
TURN = 0

POS_LEFT = [1,2,3,4,5,6,7,8,9]
POS_SEL = []
def myturn(event):
    # print("clicked at ", event.x, event.y)
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
        TURN = 0
        POS_LEFT.remove(POS)
        POS_SEL.append(POS)
    print(POS)




# Main()
root = Tk()
# Initiating Canvas...
my_canvas = Canvas(root, width = 640, height = 480, background = 'white')
my_canvas.pack()
root.bind("<Button-1>", myturn)
if TURN == 0:
    sleep(3)
    TURN = 1
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


if(TURN == 1):
    my_canvas.create_text(40, 15, text = 'YOUR TURN')
else:
    my_canvas.create_text(40, 15, text = "MY TURN.")

root.mainloop()