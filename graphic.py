import fltk

def win_screen(largeur, hauteur):
    fltk.texte(largeur/2, hauteur/2, 'You Win!',
               couleur='black', ancrage='center', police='Helvetica', taille=26, tag='')
    fltk.texte((largeur/2)-2, (hauteur/2)-1, 'You Win!',
               couleur='pink', ancrage='center', police='Helvetica', taille=24, tag='')
    fltk.texte((largeur/2)+2, (hauteur/2)+1, 'You Win!',
               couleur='magenta', ancrage='center', police='Helvetica', taille=24, tag='')
    fltk.texte(largeur/2, hauteur/2, 'You Win!',
               couleur='red', ancrage='center', police='Helvetica', taille=24, tag='')


def solv_id(largeur, hauteur, S):
    fltk.efface('solv')
    fltk.texte(largeur - (largeur*80)/100, hauteur - (hauteur*10)/100, str(S),
               couleur='red', ancrage='center', police='Helvetica', taille=24, tag='solv')



def sheep_grass(largeur, hauteur, moutons, liste):
    fltk.efface('grass')
    for elem in moutons:
        x, y = elem
        if liste[y][x] == 2:
            fltk.rectangle(x * (largeur / len(liste[0])),
                           y * (hauteur / len(liste)),
                           x * (largeur / len(liste[0])) + (20*largeur)/100,
                           y * (hauteur / len(liste)) + (20*hauteur)/100,
                           couleur='black', remplissage='#EEEEEE', epaisseur=3, tag='grass')
            fltk.image(x * (largeur / len(liste[0])) + (largeur / len(liste[0]))/2,
                       y * (hauteur / len(liste)) + (hauteur / len(liste))/2,
                       'C:/Users/guill/PycharmProjects/Project/Fichiers fournis/media/sheep_grass.png',
                       ancrage='center', tag='grass')