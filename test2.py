import fltk


"""
def bub_sort_hor(liste):
    "Tri la liste par ordre de croissance des premières coordonnées."

    for i in range(len(liste) - 1, 0, -1):
        for j in range(i):
            x, y = liste[j]
            xo, yo = liste[j + 1]
            if x > xo:print(moutons)
                liste[j + 1], liste[j] = (x, y), (xo, yo)
            elif x == xo:
                liste[j], liste[j + 1] = bub_sort_ver([liste[j], liste[j + 1]])
    return liste

def bub_sort_ver(liste):
    "Tri la liste par ordre de croissance des secondes coordonnées."

    for i in range(len(liste) - 1, 0, -1):
        for j in range(i):
            x, y = liste[j]
            xo, yo = liste[j + 1]
            if y > yo:
                liste[j + 1], liste[j] = (x, y), (xo, yo)
            elif y == yo:
                liste[j], liste[j + 1] = bub_sort_hor([liste[j], liste[j + 1]])
    return liste
"""


largeur = 800
hauteur = 600





def déplacement(elem, direction, lst):
    "Déplace le moutons donné le plus possible dans la direction donnée."

    x, y = elem
    if direction == 'Right':
        for i in range(len(lst[0])):
            if x < len(lst[0])-1 and lst[y][x+1] != 1:
                x += 1
            else:
                return x, y
    elif direction == 'Left':
        for i in range(x):
            if x > 0 and lst[y][x-1] != 1:
                x -= 1
            else:
                return x, y
    elif direction == 'Up':
        for i in range(x):
            if y > 0 and lst[y-1][x] != 1:
                y -= 1
            else:
                return x, y
    elif direction == 'Down':
        for i in range(len(lst)):
            if y < len(lst)-1 and lst[y+1][x] != 1:
                y += 1
            else:
                return x, y

    return x, y

def hor(tuples):
    return tuples[0]

def ver(tuples):
    return tuples[1]


def sheep(moutons, direction, lst):
    """Déplace les moutons dans l'ordre qui convient ."""

    print("init:", moutons)
    if direction == 'Left' or direction == 'Right':
        if direction == 'Right':
            moutons.sort(reverse=True, key=hor)
        elif direction == 'Right':
            moutons.sort(reverse=False, key=hor)
        print("sort:", moutons)
        for i in range(len(moutons)):
                moutons[i] = déplacement(moutons[i], direction, lst)

    elif direction == 'Up' or direction == 'Down':
        if direction == 'Right':
            moutons.sort(reverse=False, key=ver)
        elif direction == 'Right':
            moutons.sort(reverse=True, key=ver)
        print("sort:", moutons)
        for i in range(len(moutons)):
            moutons[i] = déplacement(moutons[i], direction, lst)

    return moutons


def emplacement_moutons(moutons):
    """Place les moutons sur le plateau."""
    
    fltk.efface('sheep')
    for elem in moutons:
        x, y = elem
        fltk.image(x * (largeur/len(liste[0])), 
                   y * (hauteur/len(liste)),
                   "./media/sheep.png", "nw", tag="sheep")
    return None


def lignes(liste):
    """Dessine les ligne du plateau."""
    
    for i in range(1, len(liste)):
        fltk.ligne(0, i * hauteur / len(liste), largeur, i * hauteur / len(liste), epaisseur=3)

    for i in range(1, len(liste[0])):
        fltk.ligne(i * largeur / len(liste[0]), 0, i * largeur / len(liste[0]), hauteur, epaisseur=3)
    return None


def items(liste):
    """Place les buissons et les herbes."""
    
    for i in range(len(liste)):
        for j in range(len(liste[i])):
            if liste[i][j] == "B":
                fltk.image((j * largeur)/len(liste[0]),
                           (i * hauteur)/len(liste),
                           "./media/bush.png", "nw")
            elif liste[i][j] == "G":
                fltk.image((j * largeur)/len(liste[0]),
                           (i * hauteur)/len(liste),
                           "./media/grass.png", "nw")
    return None


def test(moutons, liste):
    fltk.cree_fenetre(largeur, hauteur)
    lignes(liste)
    items(liste)
    emplacement_moutons(moutons)
    t = 0
    while t < 100:
        
        direction = fltk.touche(fltk.attend_ev())
        sheep(moutons, direction, liste)
        emplacement_moutons(moutons)
        t += 1
    fltk.attend_fermeture()

def check_win(moutons, liste):
    pass
"""
    for elems in liste:
        for elemss in elems:
            if elemss == 'G':
                for elem in moutons:
                    if elem == elemss:
"""





liste = [[None, 'B', None, None, None],
         ['B', 'B', None, None, None],
         [None, 'G', 'B', 'B', None],
         [None, 'B', 'G', None, None],
         [None, None, None, 'B', None]]

moutons = [(0, 2), (3, 1), (4, 2), (4, 4)]



test(moutons, liste)
"""
fltk.cree_fenetre(largeur, hauteur)
direction = fltk.touche(fltk.attend_ev())
print(direction)
sheep(moutons, direction, liste)
fltk.ferme_fenetre()
"""

