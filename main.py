from fltk import abscisse_souris, attend_clic_gauche, attend_ev, attend_fermeture, cree_fenetre, donne_ev, efface, efface_tout, image, mise_a_jour, ordonnee_souris, taille_texte, texte, touche, type_ev
import plateau
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

def settings():

    path = os.path.abspath('./maps')
    sys.path.append(path)
    for i, elem in enumerate(os.listdir(path)):
        attend_ev()
        texte(largeur//2, hauteur*0.1*i + 100, elem, ancrage='center')
    return os.listdir(path)

def menu():

    image(largeur//2 , hauteur*1/7, "./media/peesh.png", "nw")
    image(largeur//20, hauteur*1/3, "./jouer.png", "nw")
    image(largeur//2, hauteur*1/7 + 10, "./media/grass.png", "sw")
    image(largeur//20, hauteur//2, "./Settings.png", "nw")
    image(largeur//20, hauteur//1.5, "./Quitter.png", "nw")


def jeu(moutons, liste):
    win = grass.condition(liste)
    plateau.lignes(largeur, hauteur, liste)
    plateau.items(largeur, hauteur, liste)
    plateau.emplacement_moutons(largeur, hauteur, moutons, liste)
    t = False
    while t != True :
        direction = touche(attend_ev())
        moutons = sheep.Direction(moutons, direction, liste)
        plateau.emplacement_moutons(largeur, hauteur, moutons, liste)
        solu = grass.grass(largeur, hauteur, moutons, liste)
        print(solu)
        if solu == win:
            t = True
    texte(largeur/2, hauteur/2, 'You Win!',
                    couleur='red', ancrage='center', police='Helvetica', taille=24, tag='')

    return None


if __name__ == "__main__":

    cree_fenetre(largeur, hauteur)
    menu()
    while True:

        mise_a_jour()
        ev = donne_ev()
        tev = type_ev(ev)

        
        
        if tev == 'ClicGauche':
            if zone_clic_menu((largeur//20, hauteur//3),"Jouer"):
                efface_tout()
                liste, moutons = grass.creation("./maps/square/map1.txt")
                jeu(moutons, liste)

            if zone_clic_menu((largeur//20, hauteur//2), 'Settings'):
                efface_tout()
                path = os.path.abspath('./maps')
                sys.path.append(path)

                for i, elem in enumerate(os.listdir(path)):
                    texte(largeur//2, hauteur*0.1*i + 100, elem, ancrage='center', tag=str(i))
                
                while True:

                    mise_a_jour()
                    ev = donne_ev()
                    tev = type_ev(ev)

                    if tev == 'ClicGauche':

                        if zone_clic_menu((largeur//2, 100), 'BIG MAPS'):
                            efface_tout()
                            path = os.path.abspath('./maps/big')
                            sys.path.append(path)
                            for i, elem in enumerate(os.listdir(path)):
                                texte(largeur*0.9, hauteur*0.1*i + 100, elem, ancrage='center', tag=str(i))

                            while True:

                                mise_a_jour()
                                ev = donne_ev()
                                tev = type_ev(ev)

                                if tev == 'ClicGauche':
                                    for i in range(1, len(os.listdir(path))+1):
                                        if zone_clic_menu((largeur*0.9, hauteur*0.1*(i-1) + 100), "len de map"):
                                            efface_tout()
                                            liste, moutons = grass.creation(f"./maps/big/big{i}.txt")
                                            jeu(moutons, liste)
                                            attend_clic_gauche()
                                            efface_tout()
                                            menu()
                                            break
                                    break
                        ###TRANSITION##
                        if zone_clic_menu((largeur//2, hauteur*0.1 + 100), "MAP GRP"):
                            efface_tout()
                            path = os.path.abspath('./maps/map_grp')
                            sys.path.append(path)
                            for i, elem in enumerate(os.listdir(path)):
                                texte(largeur*0.9, hauteur*0.1*i + 100, elem, ancrage='center')

                            while True:

                                mise_a_jour()
                                ev = donne_ev()
                                tev = type_ev(ev)
                
                                if tev == 'ClicGauche':
                                    for i in range(1, len(os.listdir(path))+1):
                                        if zone_clic_menu((largeur*0.9, hauteur*0.1*(i-1) + 100), "len de map"):
                                            efface_tout()
                                            liste, moutons = grass.creation(f"./maps/map_grp/map{i}.txt")
                                            jeu(moutons, liste)
                                            attend_ev()
                                            efface_tout()
                                            menu()
                                            break
                                    break
                        ###TRANSITION##                
                        if zone_clic_menu((largeur//2, hauteur*0.2 + 100), "SQUARE MAPS"):
                            efface_tout()
                            path = os.path.abspath('./maps/square')
                            sys.path.append(path)
                            for i, elem in enumerate(os.listdir(path)):
                                texte(largeur*0.9, hauteur*0.1*i + 100, elem, ancrage='center')

                            while True:

                                mise_a_jour()
                                ev = donne_ev()
                                tev = type_ev(ev)
                
                                if tev == 'ClicGauche':
                                    for i in range(1, len(os.listdir(path))+1):
                                        if zone_clic_menu((largeur*0.9, hauteur*0.1*(i-1) + 100), "len de map"):
                                            efface_tout()
                                            liste, moutons = grass.creation(f"./maps/square/map{i}.txt")
                                            jeu(moutons, liste)
                                            attend_ev()
                                            efface_tout()
                                            menu()
                                            break
                                    break
                        ###TRANSITION##
                        if zone_clic_menu((largeur//2, hauteur*0.3 + 100), "TESTS MAPS"):
                            efface_tout()
                            path = os.path.abspath('./maps/tests')
                            sys.path.append(path)
                            for i, elem in enumerate(os.listdir(path)):
                                texte(largeur*0.9, hauteur*0.1*i + 100, elem, ancrage='center')

                            while True:

                                mise_a_jour()
                                ev = donne_ev()
                                tev = type_ev(ev)

                                if tev == 'ClicGauche':
                                    for i in range(1, len(os.listdir(path))+1):
                                        if zone_clic_menu((largeur*0.9, 100), "len de map"):
                                            efface_tout()
                                            liste, moutons = grass.creation(f"./maps/tests/losable.txt")
                                            jeu(moutons, liste)
                                        if zone_clic_menu((largeur*0.9, hauteur*0.1 + 100), "len de map"):
                                            efface_tout()
                                            liste, moutons = grass.creation(f"./maps/tests/test_move.txt")
                                            jeu(moutons, liste)
                                        attend_ev()
                                        efface_tout()
                                        menu()
                                        break
                                    break
                        ###TRANSITION##
                        if zone_clic_menu((largeur//2, hauteur*0.4 + 100), "theme maps"):
                            efface_tout()
                            path = os.path.abspath('./maps/theme')
                            sys.path.append(path)
                            for i, elem in enumerate(os.listdir(path)):
                                texte(largeur*0.9, hauteur*0.1*i + 100, elem, ancrage='center')

                            while True:

                                mise_a_jour()
                                ev = donne_ev()
                                tev = type_ev(ev)
                
                                if tev == 'ClicGauche':
                                    for i in range(1, len(os.listdir(path))):
                                        if zone_clic_menu((largeur*0.9, hauteur*0.1*(i-1) + 100), "len de map"):
                                            efface_tout()
                                            liste, moutons = grass.creation(f"./maps/theme/one_sheep{i}.txt")
                                            jeu(moutons, liste)
                                            break
                                        if zone_clic_menu((largeur*0.9, hauteur*0.1*(2) + 100), "onegrass.txt"):
                                            efface_tout()
                                            liste, moutons = grass.creation(f"./maps/theme/onegrass.txt")
                                            jeu(moutons, liste)
                                            break
                                        attend_ev()
                                        efface_tout()
                                        menu()
                                    break
                        ###TRANSITION##
                        if zone_clic_menu((largeur//2, hauteur*0.5 + 100), "wide maps"):
                            efface_tout()
                            path = os.path.abspath('./maps/wide')
                            sys.path.append(path)
                            for i, elem in enumerate(os.listdir(path)):
                                texte(largeur*0.9, hauteur*0.1*i + 100, elem, ancrage='center')
                            
                            while True:

                                mise_a_jour()
                                ev = donne_ev()
                                tev = type_ev(ev)
                
                                if tev == 'ClicGauche':
                                    for i in range(1, len(os.listdir(path))+1):
                                        if zone_clic_menu((largeur*0.9, hauteur*0.1*(i-1) + 100), "map num X"):
                                            efface_tout()
                                            liste, moutons = grass.creation(f"./maps/wide/wide{i}.txt")
                                            jeu(moutons, liste)
                                            attend_clic_gauche()
                                            efface_tout()
                                            menu()
                                            mise_a_jour()
                                            break
                                    break
                        ###TRANSITION##
                        
                        
                        
                    mise_a_jour()
                    if tev == 'ClicDroit':
                        efface_tout()
                        menu()
                        break
                    
            if zone_clic_menu((largeur//20, hauteur//1.5), "Quitter"):
                efface_tout()
                mise_a_jour()
                exit()

        if tev == "ClicDroit":
            efface_tout()
            menu()
