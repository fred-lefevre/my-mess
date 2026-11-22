# fic_info_vider.py
import os
from fic_info_config import FICHIER
from fic_info_outils import verifier_existence_fichier

verifier_existence_fichier(FICHIER)

# Ouverture en mode "w" (write) :
# Comme le fichier existe déjà, il est vidé
fic = open(FICHIER, "w", encoding="utf8")
fic.close()
print(f"Le fichier \"{FICHIER}\" a été vidé !")
