# masquage-numpy.py

import numpy as np

notes = np.array([10, 15.5, 6, -3, 8, -5, 13])
print("Notes", notes)
etudiants = np.array(['Bobby', 'Tara', 'Solveig', 'Bobby', 'Tara', 'Tara', 'Bobby'])
print("Étudiants", etudiants)

# Condition testée sur chaque élément et recupération du résultat
masque_notes_ok = notes >= 0
print("Masque notes valides", masque_notes_ok)
# Application du masque
print("Notes valides", notes[masque_notes_ok])

masque_notes_tara = etudiants == 'Tara'
print("Masque notes de Tara", masque_notes_tara)
print("Notes de Tara", notes[masque_notes_tara])

masque_notes_tara_ok = (notes >= 0) & (etudiants == 'Tara')
print("Masque notes valides de Tara", masque_notes_tara_ok)
print("Notes valides de Tara", notes[masque_notes_tara_ok])
