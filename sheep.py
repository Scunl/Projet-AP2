
def hor(tuples):
    return tuples[0]

def ver(tuples):
    return tuples[1]


def Droite(moutons, lst):
    """Déplace vers l'est."""

    
    moutons.sort(reverse=True, key=hor)
    
    for i in range(len(moutons)):
        x, y = moutons[i]
        for j in range(len(lst[0])):
            if x < len(lst[0])-1 and lst[y][x+1] != 1 and (x+1, y) not in moutons:
                x += 1
            else:
                moutons[i] = (x, y)
    return moutons

def Gauche(moutons, lst):
    """Déplace vers l'ouest."""

    
    moutons.sort(reverse=False, key=hor)
    
    for i in range(len(moutons)):
        x, y = moutons[i]
        for j in range(len(lst[0])):
            if x > 0 and lst[y][x - 1] != 1 and (x - 1, y) not in moutons:
                x -= 1
            else:
                moutons[i] = (x, y)
    return moutons

def Haut(moutons, lst):
    """Déplace vers le nord."""

    
    moutons.sort(reverse=False, key=ver)
    
    for i in range(len(moutons)):
        x, y = moutons[i]
        for j in range(len(lst)):
            if y > 0 and lst[y - 1][x] != 1 and (x, y - 1) not in moutons:
                y -= 1
            else:
                moutons[i] = (x, y)
    return moutons

def Bas(moutons, lst):
    """Déplace vers le sud."""

    
    moutons.sort(reverse=True, key=ver)
    
    for i in range(len(moutons)):
        x, y = moutons[i]
        for j in range(len(lst)):
            if y < len(lst)-1 and lst[y + 1][x] != 1 and (x, y + 1) not in moutons:
                y += 1
            else:
                moutons[i] = (x, y)
    return moutons


def Direction(moutons, direction, lst):
    """Analise la direction donnée et déplace les moutons dans cette direction."""

    if direction == 'Right':
        moutons = Droite(moutons, lst)
    elif direction == 'Left':
        moutons = Gauche(moutons, lst)
    elif direction == 'Up':
        moutons = Haut(moutons, lst)
    elif direction == 'Down':
        moutons = Bas(moutons, lst)
    return moutons
