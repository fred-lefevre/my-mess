# exception-nombre.py
#
# Frederic Lefevre <fred.lefevre@gmail.com>

try:
    # Code à exécuter
    choix = input("Choisissez un nombre entier : ")
    nb = int(choix)
    inverse = 1 / nb
    print("Son inverse est", inverse)
except ValueError:
    # Quand est-ce que cette instruction est exéctuée ?
    #
    print("Il fallait choisir un nombre")
except:
    # Quand est-ce que cette instruction est exéctuée ?
    #
    print("Un autre problème est survenu")
else:
    # Quand est-ce que cette instruction est exéctuée ?
    #
    print("Tout s'est bien déroulé")
finally:
    # Quand est-ce que cette instruction est exéctuée ?
    #
    print("Bye bye")
