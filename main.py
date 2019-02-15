from time import sleep

from PIL import Image
import pyscreenshot as ImageGrab
import uinput
import os

clickPos = []
offset_x = 760
offset_y = 820

def getTiles(image):
    row = 3
    width = 100
    height = 150
    board = []

    for i in range(4) :
        y = 150 * row
        col =3
        row-= 1
        for j in range(4) :
            x = 100 * col
            col -= 1
            box = (x, y, width+x, height+y)
            clickPos.append([x+50, y-50])
            board.append(image.crop(box))
    return board

def checkBlack(gameBoard):
    i = 0
    pos = []
    for image in gameBoard:
        pix = image.load()
        pix = pix[20,20]
        if(pix[0] < 30):
            print("FOUND BLACK AT POS: " + str(i) )
            pos.append(i)
        i+=1
    return pos


def grabScreenShot():
    im = ImageGrab.grab(bbox=(750, 280, 1160, 910))  # X1,Y1,X2,Y2
    box = (0,0,400,600)
    im.crop(box)
    im.show()
    return im

def convertPos(pos):
    return clickPos[pos]

def click(x,y):
    os.system("xdotool mousemove %s %s " % (str(x + offset_x),str(y +offset_y)))
    print("click at %s %s " % (str(x + offset_x),str(y +offset_y)))
    os.system("xdotool click 1")

def clearBoard(board):

    black_keys_pos = checkBlack(board)

    for key in black_keys_pos:
        click(clickPos[key][0],clickPos[key][1])





def main():
    sleep(5)
    board = getTiles(grabScreenShot())
    clearBoard(board)







if __name__ == '__main__':
    main()