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
               couleur='red', ancrage='nw', police='Helvetica', taille=20, tag='solv')
