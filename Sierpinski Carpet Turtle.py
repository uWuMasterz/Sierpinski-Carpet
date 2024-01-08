#!/usr/bin/env python3

import turtle

# --- functions ---
turtle.speed(2)
# n = level
# l = size of the picture
def s(n, l):

    if n == 0: #base case

        turtle.color('black') # set colour to black
        turtle.begin_fill() # start filling the colour
        for _ in range (4): # complete a square
            turtle.forward(l) # move forward 1 step
            turtle.left(90) # turns 90 degrees
        turtle.end_fill() # stop filling colour


    else:
        # the carpet can be split into 9 smaller sections (3x3), only draw on 8 of them

        # n-1 because the level of decreases
        # l/3 because the side of the square can be split into 3 different parts

        #draw 2 small sections then rotate left
        #Iterate the loop 3 more times to draw all 8 smaller carpets
        for _ in range(4):

            s(n-1, l/3)
            turtle.forward(l/3)


            s(n-1, l/3)
            turtle.forward(l/3)

            turtle.forward(l/3)
            turtle.left(90)


        turtle.update()

# --- main ---


turtle.tracer(0)

# start
s(1, 200)

# event loop
turtle.done()
