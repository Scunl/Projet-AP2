import fltk


def plateau(liste):

    for i in range(1, len(liste)):     
        fltk.ligne(0, i*hauteur/len(liste), largeur, i*hauteur/len(liste), epaisseur=3)

    for i in range(1, len(liste[0])):
        fltk.ligne(i*largeur/len(liste[0]),0, i*largeur/len(liste[0]), hauteur, epaisseur=3)
    return None


def jeu(liste):
    for i in range(len(liste)):
        for j in range(len(liste[i])):
            if liste[i][j] == "B":
                fltk.image(j*largeur/len(liste[0]), i*hauteur/len(liste),  "./media/bush.png", "nw")
            if liste[i][j] == "G":
                fltk.image(j*largeur/len(liste[0]), i*hauteur/len(liste),  "./media/grass.png", "nw")
    return None

def emplacement_moutons(moutons):
    """
    """
    for elem in moutons:
        y, x = elem
        fltk.image(x*largeur/len(liste[0]), y*hauteur/len(liste), "./media/sheep.png", "nw",tag="sheep")
    return None

def déplacement(liste, moutons):
    "déplace un mouton au maximum"
    for i, elem in enumerate(moutons):
        for j, elems in enumerate(moutons):
            x, y = elem
            if x < 4 and x >= 0:
                for b in range(len(liste[0])):
                    if liste[0][b] != None:
                        moutons[j] = (j, b)
                        emplacement_moutons(moutons)
            
            if y < 4:
                pass
    return None


def check(ligne):
    """
    """
    pass


if __name__ == '__main__':

    largeur = 800
    hauteur = 600
    fltk.cree_fenetre(largeur, hauteur)

    liste = [[None, 'B' , None, 'B' , None],
            ['B' , 'B' , None, None, None],
            [None, 'G' , 'B' , 'B' , None],
            [None, 'B' , 'G' , None, None],
            [None, None, None, 'B' , None]]

    moutons = [(0,4), (1,3), (2,4), (4,4)]

    plateau(liste)
    jeu(liste)
    emplacement_moutons(moutons)

    while True:
        
    ### INTERFACE MENU ###
        fltk.mise_a_jour()
        ev = fltk.donne_ev()
        tev = fltk.type_ev(ev)

        if tev == 'ClicGauche':
            direction = tev
            fltk.attend_fermeture()
