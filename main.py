from fltk import abscisse_souris, attend_clic_gauche, attend_ev, attend_fermeture, cree_fenetre, donne_ev, efface, efface_tout, image, mise_a_jour, ordonnee_souris, taille_texte, texte, touche, type_ev
import projlast
import sheep
import grass
import os
import sys

largeur = 800
hauteur = 600



def zone_clic_menu(bouton, text):
    """
    Permet de vérifier si le clic est dans la zone d'un bouton qui est un tuple
    """


    a, b = taille_texte(text)
    a1, b1 = bouton

    if (a1 - 100 <= abscisse_souris() <= a1 + a + 100) and (b1 <= ordonnee_souris() <= b1 + b):
        return True

    return False

def test(moutons, liste):
    win = grass.condition(liste)
    projlast.lignes(largeur, hauteur, liste)
    projlast.items(largeur, hauteur, liste)
    projlast.emplacement_moutons(largeur, hauteur, moutons, liste)
    t = False
    while t != True :
        direction = touche(attend_ev())
        moutons = sheep.Direction(moutons, direction, liste)
        projlast.emplacement_moutons(largeur, hauteur, moutons, liste)
        solu = grass.grass(largeur, hauteur, moutons, liste)
        print(solu)
        if solu == win:
            t = True
    texte(largeur/2, hauteur/2, 'You Win!',
                    couleur='red', ancrage='center', police='Helvetica', taille=24, tag='')
    attend_fermeture()

if __name__ == "__main__":



    cree_fenetre(largeur, hauteur)
    image(largeur//2 , hauteur*1/7, "./media/peesh.png", "nw")
    image(largeur//20, hauteur*1/3, "./jouer.png", "nw")
    image(largeur//2, hauteur*1/7 + 10, "./media/grass.png", "sw")
    image(largeur//20, hauteur//2, "./Settings.png", "nw")
    image(largeur//20, hauteur//1.5, "./Quitter.png", "nw")

    while True:

        mise_a_jour()
        ev = donne_ev()
        tev = type_ev(ev)

        
        
        if tev == 'ClicGauche':
            if zone_clic_menu((largeur//20, hauteur//3),"Jouer"):
                efface_tout()
                liste, moutons = grass.creation("./maps/square/map1.txt")
                test(moutons, liste)
            if zone_clic_menu((largeur//20, hauteur//2), 'Settings'):
                efface_tout()
                path = os.path.abspath('./maps')
                sys.path.append(path)
                for i, elem in enumerate(os.listdir(path)):
                    texte(largeur//2, hauteur*0.1*i + 100, elem, ancrage='center', tag=str(i))
                
                if zone_clic_menu((largeur//2, hauteur//2), "Taille de l'élément"):
                    print("test1")
                    mise_a_jour()
                    efface_tout()
                    path = os.path.abspath(f'./maps/{path[i]}')
                    sys.path.append(path)
                    
            if zone_clic_menu((largeur//20, hauteur//1.5), "Quitter"):
                efface_tout()
                mise_a_jour()
                exit()











