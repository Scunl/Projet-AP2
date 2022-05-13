import fltk
import projlast
import sheep
import grass





liste, moutons = grass.creation("./maps/big/big1.txt")


def test(moutons, liste):
    largeur = 1200
    hauteur = 800
    win = grass.condition(liste)
    fltk.cree_fenetre(largeur, hauteur)
    projlast.lignes(largeur, hauteur, liste)
    projlast.items(largeur, hauteur, liste)
    projlast.emplacement_moutons(largeur, hauteur, moutons, liste)
    t = False
    while t != True :
        direction = fltk.touche(fltk.attend_ev())
        moutons = sheep.Direction(moutons, direction, liste)
        projlast.emplacement_moutons(largeur, hauteur, moutons, liste)
        solu = grass.grass(largeur, hauteur, moutons, liste)
        print(solu)
        if solu == win:
            t = True
    fltk.texte(largeur/2, hauteur/2, 'You Win!',
                    couleur='red', ancrage='center', police='Helvetica', taille=24, tag='')
    fltk.attend_fermeture()




test(moutons, liste)










