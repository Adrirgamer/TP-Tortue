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
        
def polygone(longueur, nb_cotes):
    t.hideturtle()
    for _ in range(nb_cotes):
        t.forward(longueur)
        t.left(360/nb_cotes)
        
      
polygone(int(input("longueur:")), int(input("nb_cotes:")))
turtle.exitonclick()