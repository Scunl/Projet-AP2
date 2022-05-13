import fltk


def creation(choix_map):

    file = open(choix_map)
    lines = file.readlines()
    
    file.close()

    liste = []
    moutons = []
    for i, line in enumerate(lines):
        liste.append([])
        for j in range(len(lines)):
            if line[j] == "_":
                liste[i].append(0)
            elif line[j] == "S":
                moutons.append((j, i))
                liste[i].append(0)
            elif line[j] == "B":
                liste[i].append(1)
            elif line[j] == "G":
                liste[i].append(2)
        
    return liste, moutons

liste, moutons = creation("./maps/big/big1.txt")

def grass(largeur, hauteur, moutons, liste):
    fltk.efface('grass')
    solu = 0
    for elem in moutons:
        x, y = elem
        if liste[y][x] == 2:
            fltk.rectangle(x * (largeur / len(liste[0])),
                           y * (hauteur / len(liste)),
                           x * (largeur / len(liste[0])) + (20*largeur)/100,
                           y * (hauteur / len(liste)) + (20*hauteur)/100,
                           couleur='black', remplissage='#FF1000', epaisseur=3, tag='grass')
            fltk.image(x * (largeur / len(liste[0])) + (largeur / len(liste[0]))/2,
                       y * (hauteur / len(liste)) + (hauteur / len(liste))/2,
                       './media/sheep_grass.png',
                       ancrage='center', tag='grass')
            solu += 1
    return solu



def condition(lst):
    tot = 0
    for i in lst:
        for j in i:
            if j == 2:
                tot += 1
    return tot









