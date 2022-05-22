from tabnanny import check
from turtle import back
from fltk import abscisse_souris, attend_clic_gauche, attend_ev, attend_fermeture, cree_fenetre, donne_ev, efface, efface_tout, image, mise_a_jour, ordonnee_souris, taille_texte, texte, touche, type_ev
import plateau
import sheep
import grass
import os
import sys
import graphic

largeur = 1000
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
    image(largeur//20, hauteur//2, "./Quitter.png", "nw")
    
    return None





def jeu(moutons, liste):
    """Fonction principal permettant de lancer une map et jouer choisit au préalable."""
    win = grass.condition(liste)
    plateau.lignes(largeur, hauteur, liste)
    plateau.emplacement_objet(largeur, hauteur, liste)
    plateau.emplacement_moutons(largeur, hauteur, moutons, liste)
    t = False
    while t != True :

        mise_a_jour()
        ev = donne_ev()
        tev = type_ev(ev)

        if tev == 'ClicGauche':
            efface_tout()
            t = True
            menu()
            

        direction = touche(attend_ev())
        moutons = sheep.Direction(moutons, direction, liste)
        plateau.emplacement_moutons(largeur, hauteur, moutons, liste)
        solu = grass.sheep_grass(largeur, hauteur, moutons, liste)
        if solu == win:
            t = True
            graphic.win_screen(largeur, hauteur)
            attend_clic_gauche()

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
                    print(doublons(catastrophe1(liste, moutons)))
                    jeu(moutons, liste)
                    jeua = 0


def principal():
    """Permet d'être redirigé vers la selection de map ou quitter le jeu."""
    
    
    while True:

        mise_a_jour()
        ev = donne_ev()
        tev = type_ev(ev)

        
        
        if tev == 'ClicGauche':
            if zone_clic_menu((largeur//20, hauteur//3),"Jouer"):
                efface_tout()
                type_map()
                break

            if zone_clic_menu((largeur//20, hauteur//2), "Quitter"):
                efface_tout()
                mise_a_jour()
                exit()

def check_win(liste, moutons):
    """Permet de vérifier si le nombre de case grass est égale au nombre de moutons sur une case grass.
    Retourne True si c'est égal et False à l'inverse"""
    a = 0
    for elem in moutons:

        y, x = elem
        if liste[x][y] == 2:
            a = a + 1
        if a == grass.condition(liste):
            return True
    return False
    


def catastrophe1(plateau, moutons, visite=None):
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
        moutons = moutons.copy()
        sheep.Direction(moutons, i, plateau)
        s = catastrophe1(plateau, moutons, visite)
        if s != None:
            return [i] + s
        moutons = temp
    return None

def catastrophe2(liste, moutons):
    visite = set()
    a_traiter = [(moutons, [])]
    while len(a_traiter) != 0:
        temp = a_traiter.pop(0)
        if check_win(liste, temp[0]):
            return temp[1]
        if tuple(temp[0]) in visite:
            del a_traiter[0]
        else:
            visite.add(tuple(temp[0]))
            for direction in ['Down', 'Right', 'Up', 'Left']:
                temp2 = temp[0].copy()
                sheep.Direction(temp2, direction, liste)
                a_traiter.append((temp2, temp[1] + [direction]))
    return None

def doublons(liste):
    liste2 = []
    if not liste:
        return None
    liste2.append(liste[0])
    for i in range(1, len(liste)):
        if liste[i] != liste[i-1]:
            liste2.append(liste[i])
    return liste2





if __name__ == "__main__":

    cree_fenetre(largeur, hauteur)
    while True:
        efface_tout()
        menu()
        principal()
        