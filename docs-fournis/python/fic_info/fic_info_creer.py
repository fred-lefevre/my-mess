# fic_info_creer.py
import os
from fic_info_config import FICHIER
from fic_info_outils import verifier_absence_fichier

verifier_absence_fichier(FICHIER)

# Ouverture en mode "w" (write) :
# Comme le fichier n'existe pas, il est créé
fic = open(FICHIER, "w", encoding="utf8")
fic.close()
print(f"Le fichier \"{FICHIER}\" a été créé !")
