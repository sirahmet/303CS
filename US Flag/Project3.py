# File: Project3.py
# Student: Ahmet Nalcaci
# UT EID: an27394
# Course Name: CS303E
# Unique Number: 50695
#
# Date Created: 12/2/2020
# Date Last Modified: 12/4/2020
# Description of Program: Draws American Flag

import turtle

Bob = turtle.Turtle()
Bob.speed(10)
Bob.penup()

# starting points (0,0)
xValue = 0        
yValue = 0      


def fillRectangle(x, y, height, width, color):
    Bob.penup()
    Bob.goto(x,y)
    Bob.pendown()
    Bob.color(color)
    Bob.begin_fill()

    for _ in range(2):
        Bob.forward(width)
        Bob.right(90)
        Bob.forward(height)
        Bob.right(90)
    Bob.penup()
    Bob.end_fill()


def drawStar(x,y,color,length):
    Bob.penup()
    Bob.goto(x,y)
    Bob.setheading(0)
    Bob.pendown()
    Bob.begin_fill()
    Bob.color(color)
    for _ in range(0,5) :
        Bob.forward(length)
        Bob.right(144)
        Bob.forward(length)
        Bob.right(144)
    Bob.end_fill()
    Bob.penup()


def stripes(stripeHeight, flagWidth):
    x = xValue
    y = yValue
    # Make 6 red and 6 white stripes     
    for _ in range(0,6):
        for color in ["red", "white"]:
            fillRectangle(x, y, stripeHeight, flagWidth, color)
            # Makes space between stripeHeight
            y = y - stripeHeight            
    # Add the last red stripe
    fillRectangle(x, y, stripeHeight, flagWidth, "red")
    y = y - stripeHeight


def miniSquare(flagHeight):
    miniSquareHeight = (7/13) * flagHeight     #The proportions were found in https://www.inchcalculator.com/american-flag-size-proportions-calculator/
    miniSquareWidth = (0.76) * flagHeight
    fillRectangle(xValue, yValue, miniSquareHeight, miniSquareWidth, "navy")


def sixStarRows(stripeHeight, starSize):
    spaceBetweenStars = 30
    spaceBetweenLines = stripeHeight + 6
    y = -13    
    # create 5 rows 
    for _ in range(0,5):
        x = 15    
        #6 stars in each row
        for _ in range (0,6):
            drawStar(x, y, "white", starSize)
            x = x + spaceBetweenStars
        y = y - spaceBetweenLines


def fiveStarRows(stripeHeight, starSize):
    spaceBetweenStars = 30
    spaceBetweenLines = stripeHeight + 6
    y = -25     
    # create 4 rows 
    for _ in range(0,4) :
        x = 31     
        # 5 stars in each row
        for _ in range (0,5) :
            drawStar(x, y, "white", starSize)
            x = x + spaceBetweenStars
        y = y - spaceBetweenLines


def main():
    #flag height to width ratio is 10:19 -Wikipedia
    flagHeight = 250
    flagWidth = 475
    stripeHeight = flagHeight/13
    starSize = 10 

    stripes(stripeHeight, flagWidth)
    miniSquare(flagHeight)
    sixStarRows(stripeHeight, starSize)
    fiveStarRows(stripeHeight, starSize)

main()

turtle.done()



