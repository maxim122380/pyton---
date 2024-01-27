from turtle import *
from random import randint
finish = 200

def startrace(t, x, y, color):
    t.color(color)
    t.shape("turtle")
    t.penup()
    t.goto(x, y)

def field():  # Отрисовка поля
    speed(0)
    def func():
        color("grey")
        left(90)
        forward(100)
        left(180)
        forward(200)
        left(90)
    x = -200
    for i in range(28):
        penup()
        goto(x, 0)
        pendown()
        func()
        x += 15
    hideturtle()

def dance(t, color):
    t.pensize(5)
    t.speed(15)
    t.penup()
    t.goto(-100,30)
    t.pendown()
    t.begin_fill()
    t.color("gold")
    for i in range(18):
        t.forward(200)
        t.left(100)
    t.end_fill()
    t.penup()
    t.goto(-30, 70)
    t.pendown()
    t.color("goldenrod")
    t.write("1", font=("Arial", 70, "normal"))
    t.penup()
    t.goto(-15,70)
    t.pendown()
    t.forward(30)
    t.left(90)
    t.forward(4)
    t.left(90)
    t.forward(30)
    t.left(90)
    t.forward(4)
    t.penup()
    t.goto(-20, 200)
    t.pendown()
    t.circle(20)
    t.color(color)
    t.penup()
    t.goto(-2,201)
    t.left(90)

field()

t1 = Turtle()
t2 = Turtle()
t3 = Turtle()

startrace(t1, -200, -20, "red")
startrace(t2,-200, 20, "green")
startrace(t3, -200, 60, "blue")

while t1.xcor() < finish and t2.xcor() < finish and t3.xcor() < finish:
    t1.forward(randint(2,7))
    t2.forward(randint(2,7))
    t3.forward(7)
max_x = max(t1.xcor(), t2.xcor(), t3.xcor())

if t1.xcor() == max_x:
    clear()
    penup()
    goto(200, 0)
    pendown()
    write("👎🏻", font=("Arial", 30, "normal"))
    exitonclick()
    dance(t1, "red")
elif t2.xcor() == max_x:
    clear()
    penup()
    goto(200, 0)
    pendown()
    write("👎🏻", font=("Arial", 30, "normal"))
    exitonclick()
    dance(t2, "green")
elif t3.xcor() == max_x:
    clear()
    penup()
    goto(200, 0)
    pendown()
    write("👎🏻", font=("Arial", 30, "normal"))
    exitonclick()
    dance(t3, "blue")

