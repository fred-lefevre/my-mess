# fic_info_outils.py
import os

def verifier_absence_fichier(f):
    """Vérification de l'absence du fichier f.
    Termine le script avec le code d'erreur 1 si f existe déjà
    """
    if os.path.isfile(f) :
        print(f"Le fichier \"{f}\" existe déjà !")
        exit(1)

def verifier_existence_fichier(f):
    """Vérification de l'existence du fichier f.
    Termine le script avec le code d'erreur 1 si f n'existe pas
    """
    if not os.path.isfile(f) :
        print(f"Le fichier \"{f}\" n'existe pas !")
        exit(1)
