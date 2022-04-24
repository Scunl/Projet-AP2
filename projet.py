import fltk


def plateau(liste):
    for i in range(1, len(liste)):     
        fltk.ligne(0, i*hauteur/len(liste), largeur, i*hauteur/len(liste), epaisseur=3)

    for i in range(1, len(liste[0])):
        fltk.ligne(i*largeur/len(liste[0]),0, i*largeur/len(liste[0]), hauteur, epaisseur=3)




def déplacement(mouton, direction, lst):
    "Déplace un moutons donné le plus possible dans la direction donnée."

    x, y = mouton
    if direction == 'Right':
        for i in range(4 - x):
            print(x)
            if lst[y][x + 1] == 'B':
                return x, y
            x += 1
        for i in range(0 + x):
            if lst[y][x - 1] == 'B':
                return x, y
            x -= 1
    elif direction == 'Up':
        for i in range(0 + y):
            if lst[y - 1][x] == 'B':
                return x, y
            y -= 1
    elif direction == 'Down':
        for i in range(4 - y):
            if lst[y + 1][x] == 'B':
                return x, y
            y += 1
    return x, y
    
def bub_sort_hor(liste):
    "Tri la liste par ordre de croissance des premières coordonnées."

    for i in range(len(liste) - 1, 0, -1):
        for j in range(i):
            x, y = liste[j]
            xo, yo = liste[j + 1]
            if x > xo:
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

def sheep(moutons, direction, lst):

    if direction == 'Left' or direction == 'Right':
        bub_sort_hor(moutons)
        print(moutons)
        for i in range(len(moutons)):
            moutons[i] = déplacement(moutons[i], direction, lst)
    elif direction == 'Up' or direction == 'Down':
        bub_sort_ver(moutons)
        print(moutons)
        for i in range(len(moutons)):
            moutons[i] = déplacement(moutons[i], direction, lst)
    return moutons

def bush(buissons):
    "affiche les buissons sur l'écran"
    for i in buissons:
        x, y = i
        fltk.image((x-1)*160+80, (y-1)*160+80, "./media/bush.png", ancrage='center')
    return None


moutons = [(0,4), (1,3), (2,4), (4,4)]

largeur = 800
hauteur = 800

liste = [[None, 'B' , None, 'B' , None],
        ['B' , 'B' , None, None, None],
        [None, 'G' , 'B' , 'B' , None],
        [None, 'B' , 'G' , None, None],
        [None, None, None, 'B' , None]]



plateau(liste)
    
