# File: GermanFlag.py
# Student: Ahmet Nalcaci
# UT EID: an27394
# Course Name: CS303E
# Unique Number: 50695
#
# Date Created: 11/27/2020
# Date Last Modified: 11/27/2020
# Description of Program: The program draws a German flag



import turtle

def  drawRectangle (ttl , x, y, width, length, color):
    ttl.penup()
    ttl.goto(x, y)
    ttl.setheading (90)
    ttl.pendown ()
    ttl.fillcolor(color)
    ttl.begin_fill()

    for _ in range (2):    # draw 4 sides:
        ttl.forward(length)   #    move  forward  length;
        ttl.right (90)          #    turn  right  90  degrees
        ttl.forward(width)
        ttl.right(90)
        
    ttl.penup()
    ttl.end_fill()


Bob = turtle.Turtle ()
Bob.speed (10)
Bob.pensize (1)
drawRectangle( Bob , 0, 0,500, 100, 'Gold')
drawRectangle( Bob, 0, 100, 500, 100, 'Red')
drawRectangle(Bob, 0, 200, 500, 100, 'Black')

turtle.done()