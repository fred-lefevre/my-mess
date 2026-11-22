# fic_info_lire.py
import os
from fic_info_config import FICHIER
from fic_info_outils import verifier_existence_fichier

verifier_existence_fichier(FICHIER)

print("Lecture ligne par ligne :")
fic = open(FICHIER, "r", encoding="utf8")
for ligne in fic:
    # ligne est un texte contenant une ligne du fichier : pour
    # commencer la première, puis la dexième, ... puis la dernière.
    # La méthode strip() permet de supprimer le retour à la ligne qui
    # est situé à la fin de ligne considérée.
    print(ligne.strip())
fic.close()

print()
print("Lecture sous forme d'un seul texte :")
fic = open(FICHIER, "r", encoding="utf8")
contenu = fic.read()
fic.close()

# contenu est un texte contenant l'intégralité du fichier.
print(contenu)
