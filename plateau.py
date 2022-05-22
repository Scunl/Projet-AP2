import fltk


def emplacement_moutons(largeur, hauteur, moutons, liste):
    """Place les moutons sur le plateau."""

    fltk.efface('sheep')
    for elem in moutons:
        x, y = elem
        fltk.image(x * (largeur / len(liste[0])) + (largeur / len(liste[0]))/2,
                   y * (hauteur / len(liste)) + (hauteur / len(liste))/2,
                   "./media/sheep.png", "center", tag="sheep")
    return None


def lignes(largeur, hauteur, liste):
    """Dessine les ligne du plateau."""

    for i in range(1, len(liste)):
        fltk.ligne(0, i * hauteur / len(liste), largeur, i * hauteur / len(liste), epaisseur=3)

    for i in range(1, len(liste[0])):
        fltk.ligne(i * largeur / len(liste[0]), 0, i * largeur / len(liste[0]), hauteur, epaisseur=3)
    return None


def items(largeur, hauteur, liste):
    """Place les buissons et les herbes."""

    for i in range(len(liste)):
        for j in range(len(liste[i])):
            if liste[i][j] == 1:
                fltk.image((j * largeur) / len(liste[0]) + (largeur / len(liste[0]))/2,
                           (i * hauteur) / len(liste) + (hauteur / len(liste))/2,
                           "./media/bush.png", "center")
            elif liste[i][j] == 2:
                fltk.image((j * largeur) / len(liste[0]) + (largeur / len(liste[0]))/2,
                           (i * hauteur) / len(liste) + (hauteur / len(liste))/2,
                           "./media/grass.png", "center")
    return None
