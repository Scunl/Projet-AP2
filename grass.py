import fltk


def creation(choix_map):
    """Permet de lire un fichier texte. Ce dernier remplace les caractères du texte en éléments du jeu."""

    file = open(choix_map)
    lines = file.readlines()
    file.close()

    liste = []
    moutons = []
    for i, ligne in enumerate(lines):
        liste.append([])
        for j in range(len(lines[i])):
            if ligne[j] == "_":
                liste[i].append(0)
            if ligne[j] == "S":
                moutons.append((j, i))
                liste[i].append(0)
            if ligne[j] == "B":
                liste[i].append(1)
            if ligne[j] == "G":
                liste[i].append(2)
    return liste, moutons


def sheep_grass(largeur, hauteur, moutons, liste):
    """Réalise un carré de côté varaible qui se place sur une case de la map lorsqu'un mouton se trouve sur une case grass."""
    fltk.efface('grass')
    solu = 0
    for elem in moutons:
        x, y = elem
        if liste[y][x] == 2:
            
            fltk.rectangle(x * (largeur / len(liste[0])),
                           y * (hauteur / len(liste)),
                           x * (largeur / len(liste[0])) + ((100/len(liste[0]))*largeur)/100,
                           y * (hauteur / len(liste)) + ((100/len(liste[0]))*hauteur)/100,
                           couleur='black', remplissage='#F0F0F0', epaisseur=3, tag='grass')
            fltk.image(x * (largeur / len(liste[0])) + (largeur / len(liste[0]))/2,
                       y * (hauteur / len(liste)) + (hauteur / len(liste))/2,
                       './media/sheep_grass.png',
                       ancrage='center', tag='grass')
            solu += 1
    return solu



def condition(lst):
    """Retourne le nombre de moutons qui sont sur une case grass"""
    tot = 0
    for i in lst:
        for j in i:
            if j == 2:
                tot += 1
    return tot






