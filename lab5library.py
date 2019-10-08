#Create a function that displays a vertical line at a given x coordinate on the gfx hat.
from gfxhat import lcd
lcd.clear()
lcd.show()

x=0
y=20

while( x <=127) :
lcd.set_pixel(x,y,1)

x = x+1

lcd.show()

def vertical(y):
while( x <=127)
lcd.show()

Create a function that displays a horizontal line at a given y coordinate.
from gfxhat import lcd
lcd.clear()
lcd.show()

y=0
x=20
While (y <=63):
lcd.set_pixel(x,y,1)

y=y+1

def horizantal(x):
while ( y <=63)
lcd.show()

#Create a function that creates a staircase starting at a specific coordinate. One stair has a width of w and a height of h.
from gfxhat import lcd


def makestep(x, y, w=20, h=20, SW=127, SH=63):
    for i in range(h):
        if y >= 0:
            lcd.set_pixel(x, y - i, 1)
        else:
            h = i
    for j in range(0, w):
        if x + j <= SW:
            lcd.set_pixel(x + j, y - h, 1)
    else:
        w = j
    return (x + w, y - h)

    if x + j <= SW:
        lcd.set_pixel(x + j, y - h, 1)
    else:
        w = j


return (x + w, y - h)


def staircase(x=20, y=63, w=10, h=10):
    while (x + w < 127 and y - h >= 0):
        x, y = makestep()
        tep(x, y, w, h)


lcd.clear()
staircase()
lcd.show()

#Create a function that displays random pixel on the screen for a given period of time specifies in seconds.
from gfxhat import lcd
import time
lcd.clear()
lcd.show()
y=22
for x in range(x,y,1)
lcd.show()
import random
between o and 128
 time.sleep(1 / 30.0)

print (random.randin 0,128)

displays random pixel

def  displayRandomPixel():
for i between o and 128
 displayRandomPixel()

#Create a function clearBacklight() that resets the backlight color.
from gfx hat import backlight
backlight.set_all(10.0,225)
backlight.show()
lcd.clear()
enter
lcd not defined
lcd.clear()
lcd.show()
def clearBacklight() :
backlight.set_all(10,0,0)
put many values in backlight set all
(225,0,0))