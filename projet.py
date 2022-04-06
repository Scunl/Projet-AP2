import fltk

def déplacement(x, y):
    "déplace un mouton au maximum"
    
    if fltk.touche_pressee('Right') == True:
        x = 5
    elif fltk.touche_pressee('Left') == True:
        x = 1
    elif fltk.touche_pressee('Up') == True:
        y = 1
    elif fltk.touche_pressee('Down') == True:
        y = 5
    return x, y
    


def sheep(x, y):
    "déplace le mouton sur l'écran"
    
    testo = 0
    while testo != 10:
        fltk.efface('sheep')
        fltk.image((x-1)*160+80, (y-1)*160+80, "./media/sheep.png", ancrage='center', tag='sheep')
        fltk.attend_ev()
        x, y = déplacement(x, y)
        testo += 1
    return None

def bush(buissons):
    "affiche les buissons sur l'écran"
    for i in buissons:
        x, y = i
        fltk.image((x-1)*160+80, (y-1)*160+80, "./media/bush.png", ancrage='center')
    return None

def test(x, y, buissons):
    fltk.cree_fenetre(800, 800)
    for i in range(5):
        fltk.ligne(i*160, 0, i*160, 800, couleur='black', epaisseur=3)
        for j in range(5):
            fltk.ligne(0, j*160, 800, j*160, couleur='black', epaisseur=3)
    bush(buissons)
    sheep(x, y)
    fltk.attend_fermeture()
    
buissons = [(2, 1), (4, 1), (1, 2), (2, 2), (3, 3), (4, 3), (2, 5), (4, 5)]


test(3, 2, buissons)





    



