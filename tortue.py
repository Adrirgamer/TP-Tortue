import turtle

t = turtle.Turtle()
        
def polygone(longueur, nb_cotes, soustrait):
    t.hideturtle()
    for _ in range(nb_cotes):
        longueur = longueur - int(soustrait)
        t.forward(int(longueur))
        t.left(360/nb_cotes)

def spirograph(longueur, rotation, couleur, soustrait, vitesse, nb_cotes):
    """longueurinit = longueur du coté inital,
       rotation = degré de rotation de chaque carré par rapport au précédent
       couleur = couleur du trait
       cran = différence de longueur a chaque coté tracé
       vitesse : vitesse du tracé
       cotés : cotés de chaque tracé (experimental
    """
 
    while True:
        t.hideturtle
        t.speed(vitesse)
        t.color(couleur)
        #t.left(rotation)  a commenter pour centrer la spirale
        for _ in range(nb_cotes):
            longueur = longueur - int(soustrait)
            t.forward(int(longueur))
            t.left(360/nb_cotes)
            t.left(rotation) # centrer la spirale 
        
def equ(longueur):
    t.hideturtle()
    polygone(longueur, 3)

def carre(longueur):
    t.hideturtle()
    polygone(longueur, 4)

#carre(float(input("longueur:")))

#equ(float(input("longueur:")))
        
spirograph(int(input("longueur initiale : ")), float(input("rotation : ")), str(input("couleur : ")) , int(input("cran : ")), int(input("vitesse : ")), int(input("cotés : ")))

#polygone(float(input("longueur : ")), int(input("nb_cotes : ")), int(input("soustrait : ")))


turtle.exitonclick()