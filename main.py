from tabnanny import check
from turtle import back
from fltk import abscisse_souris, attend_clic_gauche, attend_ev, attend_fermeture, cree_fenetre, donne_ev, efface, efface_tout, image, mise_a_jour, ordonnee_souris, taille_texte, texte, touche, type_ev
import plateau
import sheep
import grass
import os
import sys
import graphic
import time

largeur = 1920
hauteur = 1080



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
    """Affiche les differents dossier dans lesquelles il y'a un groupe de map classé par theme."""

    path = os.path.abspath('./maps')
    sys.path.append(path)
    for i, elem in enumerate(os.listdir(path)):
        texte(largeur//2, hauteur*0.1*i + 100, elem, ancrage='center')
    return os.listdir(path)

def menu():
    """Affiche le menu principal du jeu."""

    image(largeur//2 , hauteur*1/7, "./media/peesh.png", "nw")
    image(largeur//20, hauteur*1/3, "./jouer.png", "nw")
    image(largeur//2, hauteur*1/7 + 10, "./media/grass.png", "sw")
    image(largeur//20, hauteur//2, "./Settings.png", "nw")
    image(largeur//20, hauteur//1.5, "./Quitter.png", "nw")
    
    return None





def jeu(moutons, liste):
    """Fonction principal permettant de lancer une map choisit au préalable."""
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
        
        if solu == win:
            t = True


    return True

def type_map():
    """Fonction permettant d'afficher sur fltk les differents répertoire de /map ainsi que de selectionner un dossier parmis les fichiers locaux 
    depuis fltk."""

    settings()

    while True:

        mise_a_jour()
        ev = donne_ev()
        tev = type_ev(ev)
        path = None

        if tev == 'ClicGauche':
            
            if zone_clic_menu((largeur//2, 100), 'BIG MAPS'):
                efface_tout()
                path = os.path.abspath('./maps/big')
                sys.path.append(path)
                for i, elem in enumerate(os.listdir(path)):
                    texte(largeur*0.9, hauteur*0.1*i + 100, elem, ancrage='center', tag=str(i))
                

            if zone_clic_menu((largeur//2, hauteur*0.1 + 100), "MAP GRP"):
                efface_tout()
                path = os.path.abspath('./maps/map_grp')
                sys.path.append(path)
                for i, elem in enumerate(os.listdir(path)):
                    texte(largeur*0.9, hauteur*0.1*i + 100, elem, ancrage='center')

            if zone_clic_menu((largeur//2, hauteur*0.2 + 100), "SQUARE MAPS"):
                efface_tout()
                path = os.path.abspath('./maps/square')
                sys.path.append(path)
                for i, elem in enumerate(os.listdir(path)):
                    texte(largeur*0.9, hauteur*0.1*i + 100, elem, ancrage='center')
            if zone_clic_menu((largeur//2, hauteur*0.3 + 100), "TESTS MAPS"):
                efface_tout()
                path = os.path.abspath('./maps/tests')
                sys.path.append(path)
                for i, elem in enumerate(os.listdir(path)):
                    texte(largeur*0.9, hauteur*0.1*i + 100, elem, ancrage='center')
            
            if zone_clic_menu((largeur//2, hauteur*0.4 + 100), "theme maps"):
                efface_tout()
                path = os.path.abspath('./maps/theme')
                sys.path.append(path)
                for i, elem in enumerate(os.listdir(path)):
                    texte(largeur*0.9, hauteur*0.1*i + 100, elem, ancrage='center')
            
            if zone_clic_menu((largeur//2, hauteur*0.5 + 100), "wide maps"):
                efface_tout()
                path = os.path.abspath('./maps/wide')
                sys.path.append(path)
                for i, elem in enumerate(os.listdir(path)):
                    texte(largeur*0.9, hauteur*0.1*i + 100, elem, ancrage='center')
            
        if path:
            
            map(path)
            break


def map(path):
    """Fonction permettant d'ouvrir une map prise au choix de l'utilisateur tant qu'elle figure parmis les dossiers locaux."""
    jeua = 1
    while jeua:

        mise_a_jour()
        ev = donne_ev()
        tev = type_ev(ev)

        if tev == 'ClicGauche':
            for i, elem in enumerate(os.listdir(path)):
                if zone_clic_menu((largeur*0.9, hauteur*0.1*i + 100), elem):
                    efface_tout()
                    liste, moutons = grass.creation(path + "/" + elem)
                    print(solveur(liste, moutons))
                    jeu(moutons, liste)
                    jeua = 0


def principal():
    """Permet de lancer une map prédéfini, et de rediriger vers la fonction type_map() si on décide de la map qu'on lance."""
    
    
    while True:

        mise_a_jour()
        ev = donne_ev()
        tev = type_ev(ev)

        
        
        if tev == 'ClicGauche':
            if zone_clic_menu((largeur//20, hauteur//3),"Jouer"):
                efface_tout()
                liste, moutons = grass.creation("./maps/map_grp/map1.txt")
                print(solveur(liste, moutons))
                jeu(moutons, liste)
                break

            if zone_clic_menu((largeur//20, hauteur//2), 'Settings'):
                efface_tout()
                type_map()
                break

            if zone_clic_menu((largeur//20, hauteur//1.5), "Quitter"):
                efface_tout()
                mise_a_jour()
                exit()

def extraction(liste):
    """Permet d'extraire le nombre d'éléments G de la liste. Cette fonction retourne la liste des herbes sans les coordonées."""
    herbe = []
    for ligne in liste:
        for element in ligne:
            if element == 'G':
                herbe.append(element)
    return herbe

def check_win(liste, moutons):
    """Permet de vérifier si le nombre de case grass est égale au nombre de moutons sur une case grass. 
    Retourne True si c'est égal et False à l'inverse"""
    a = 0
    for emplacement in moutons:
        a, b = emplacement
        if liste[a][b] == "G":
            a += 1
    if a == len(extraction(liste)):
        return True
    return False


def solveur(plateau, moutons, visite=None):
    """Solveur permettant de trouver la solution de n'importe quelle map."""
    if visite == None:
        visite = set()
    if check_win(plateau, moutons):
        return []
    if tuple(moutons) in visite:
        return None
    visite.add(tuple(moutons))
    for i in ['Left', 'Right', 'Up', 'Down']:
        temp = list(moutons)
        sheep.Direction(moutons, i, plateau)
        print(visite)
        s = solveur(plateau, moutons, visite)
        if s != None:
            return [i] + s
        moutons = temp
    return None



if __name__ == "__main__":

    cree_fenetre(largeur, hauteur)
    while True:
        efface_tout()
        menu()
        principal()
        
        


        
        