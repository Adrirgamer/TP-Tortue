import turtle
def equ(longueur):
    t = turtle.Turtle()
    t.hideturtle()
    for _ in range(3):
        t.forward(longueur)
        t.left(120)
        t.hideturtle()
equ(float(input("longueur:")))
turtle.exitonclick()