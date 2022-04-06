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
    if fltk.touche_pressee("Right") == True:
        moutons = [(0,4), (1,4), (2, 4), (4,4)]
        fltk.efface("sheep")
        emplacement_moutons(moutons)

largeur = 800
hauteur = 600
fltk.cree_fenetre(largeur, hauteur)

liste = [[None, 'B' , None, 'B' , None],
        ['B' , 'B' , None, None, None],
        [None, 'G' , 'B' , 'B' , None],
        [None, 'B' , 'G' , None, None],
        [None, None, None, 'B' , None]]

moutons = [(0,4), (1,3), (2,4), (4,4)]

def fin():
    '''
    '''
    plateau(liste)
    jeu(liste)
    
    déplacement(liste, moutons)
        

fin()

fltk.attend_fermeture()
