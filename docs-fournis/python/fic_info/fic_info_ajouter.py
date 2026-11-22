# fic_info_ajouter.py
import os
from fic_info_config import FICHIER
from fic_info_outils import verifier_existence_fichier

verifier_existence_fichier(FICHIER)

texte = input("Texte à stocker : ")

# Ouverture en mode "a" (append) : le texte sera
# ajouté à la fin du texte dejà contenu dans le fichier.
fic = open(FICHIER, "a", encoding="utf8")

# "\n" est le caractère de fin de ligne
fic.write(texte + "\n")

# Fermeture du fichier
fic.close()
