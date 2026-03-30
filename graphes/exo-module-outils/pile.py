class Pile():
    def __init__(self):
        """Initialise une nouvelle pile vide."""
        self.elements: List = []

    def empiler(self, e):
        """Ajoute un élément au sommet de la pile."""
        self.elements.append(e)

    def depiler(self):
        """Retire et renvoie l'élément au sommet de la pile."""
        if self.est_vide():
            raise Exception("Impossible de retirer un élément d'une pile vide")
        return self.elements.pop()

    def est_vide(self):
        """Retourne True lorsque la pile est vide, False sinon."""
        return len(self.elements) == 0

    def __str__(self):
        return f"Pile : {self.elements}"

if __name__ == "__main__":
    # File d'attente pour un film
    calcul = Pile()
    print(calcul)
    calcul.empiler(7)
    calcul.empiler(4)
    calcul.empiler(5)
    print(calcul)
    nb = calcul.depiler()
    print(f"{nb} vient de sortir de la pile")
    print(calcul)
    print(f"La pile est vide ? {calcul.est_vide()}")
    nb = calcul.depiler()
    print(calcul)
    nb = calcul.depiler()
    print(calcul)
    print(f"La pile est vide ? {calcul.est_vide()}")
    
