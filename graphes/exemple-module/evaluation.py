# evaluation.py

import notes

def verifier_validite(note):
    if not notes.est_valide(note):
        print("Note non valide")
        exit(1)

print("Évaluation de Bobby.")

# Saisie des notes
hist = float(input("Note d'histoire : "))
verifier_validite(hist)
geo = float(input("Note de géographie : "))
verifier_validite(geo)
philo = float(input("Note de philosophie : "))
verifier_validite(philo)

# Calcul de la moyenne globale
moy = notes.moy2(hist, geo)
moyenne = notes.moy2coef((moy, 2), (philo, 1))[0]

# Affichage de l'évaluation
print("Le moyenne de ces notes est", round(moyenne, 2))
if moy >= 10:
    print("Bravo Bobby")
else:
    print("Tu peux faire mieux Bobby")
