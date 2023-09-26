import turtle

t = turtle.Turtle()
        
def polygone(longueur, nb_cotes, soustrait):
    t.hideturtle()
    for _ in range(nb_cotes):
        longueur = longueur - int(soustrait)
        t.forward(int(longueur))
        t.left(360/nb_cotes)

def spirograph(longueurinit, rotation, couleur, cran):
    """longueurinit = longueur du coté inital,
       rotation = degré de rotation de chaque carré par rapport au précédent
       couleur = couleur du trait
       cran = différence de longueur a chaque coté tracé
    """
   # t.hideturtle()
    for _ in range(360/int(rotation)):
        t.color(couleur)
        rotation = rotation + 360/int(rotation)
        for _ in range(4):
            longueurinit=longueurinit + int(cran)
            t.forward(longueurinit)
            t.right(rotation)

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

#carre(float(input("longueur:")))

#equ(float(input("longueur:")))
        
spirograph(int(input("longueur initiale : ")), int(input("rotation : ")), str(input("couleur : ")) , int(input("cran : ")))

#polygone(float(input("longueur : ")), int(input("nb_cotes : ")), int(input("soustrait : ")))


turtle.exitonclick()