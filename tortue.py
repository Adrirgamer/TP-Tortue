import turtle

t = turtle.Turtle()

def equ(longueur):
    t.hideturtle()
    for _ in range(3):
        t.forward(longueur)
        t.left(120)

def carre(longueur):
    t.hideturtle()
    for _ in range(4):
        t.forward(longueur)
        t.left(90)
      
carre(float(input("longueur:")))
turtle.exitonclick()