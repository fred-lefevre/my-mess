# notes.py

"""
Module de gestion de notes :
validation, calcul de moyenne, ...
"""

# Note minimale valide
NOTE_MINI = 0

# Note maximale valide
NOTE_MAXI = 20

def est_valide(note):
    """
    Permet de savoir si une note est valide ou non.
    
    Paramètre :
        note (float) : Une note à valider
    
    Retourne :
        (bool) True lorsque note est valide, False sinon
    """
    return NOTE_MINI <= note <= NOTE_MAXI

def moy2(na, nb):
    """
    Permet de calculer la moyenne de deux notes
    
    Paramètre :
        na (int ou float) : une note
        nb (int ou float) : une autre note

    Retourne :
        (float) la moyenne des deux notes
    """
    return (na + nb) / 2

def moy2coef(na, nb):
    """
    Permet de calculer la moyenne pondérée de deux notes
    
    Paramètre:
        na (tuple) : (une note, son coefficient)
        nb (tuple) : (une autre note, son coefficient)

    Retourne :
        (float) la moyenne des deux notes
    """
    assert(type(na) == tuple)
    assert(type(nb) == tuple)
    coef = na[1] + nb[1]
    return ((na[0] * na[1] + nb[0] * nb[1]) / coef, float(coef))

if __name__ == "__main__":
    print("Utilisation directe du fichier :", __file__) 
    
    # Assertions exécutées uniquement si le présent fichier est interprété directement,
    # c'est_à_dire sans être utilisé come un module.
    assert est_valide(12.7), "12.7 est une note valide"
    assert est_valide(0), "0 est une note valide"
    assert est_valide(20), "20 est une note valide"
    assert not est_valide(-1), "-1 est une note non valide"
    assert not est_valide(25), "25 est une note non valide"
    assert moy2(11, 12) == 11.5, "La moyenne de 11 et de 12 est 11.5"
    assert moy2(12, 11) == 11.5, "La moyenne de 12 et de 11 est 11.5"
    assert moy2coef((12, 2), (6, 1))[0] == 10, "La moyenne de 12 coef 2 et de 6 coef est 10"
    # ...    
