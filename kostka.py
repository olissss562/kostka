from turtle import Turtle
import random


turtle1 = Turtle()
turtle1.speed(999)

def ctverec():
    for n in range(4):
        turtle1.forward(100)
        turtle1.right(90)


def vykresli_cislo(cislo):
    ctverec()
    vzdalenost = 100/(cislo+1)
    for i in range(cislo):
        turtle1.penup()
        turtle1.forward(vzdalenost)
        turtle1.right(90)
        turtle1.forward(20)
        turtle1.pendown()
        turtle1.forward(60)
        turtle1.penup()
        turtle1.forward(20)
        turtle1.left(180)
        turtle1.forward(100)
        turtle1.right(90)
        turtle1.pendown()
    turtle1.right(180)
    turtle1.forward(100 - vzdalenost)
    turtle1.left(180)





vykresli_cislo(random.randint(1, 6))
turtle1.penup()
turtle1.forward(150)
turtle1.pendown()
vykresli_cislo(random.randint(1, 6))


input()