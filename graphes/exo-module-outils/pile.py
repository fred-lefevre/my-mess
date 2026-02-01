from typing import TypeVar, Generic

# Tous les éléments de la pile seront d'un même type T.
T = TypeVar('T')

class Pile(Generic[T]):
    def __init__(self) -> None:
        """Initialise une nouvelle pile vide."""
        # On précise que c'est une liste d'éléments de type T
        self.elements: List[T] = []

    def empiler(self, e: T) -> None:
        """Ajoute un élément au sommet de la pile."""
        self.elements.append(e)

    def depiler(self) -> T:
        """Retire et renvoie l'élément au sommet de la pile."""
        if self.est_vide():
            raise Exception("Impossible de retirer un élément d'une pile vide")
        return self.elements.pop()

    def est_vide(self) -> bool:
        """Retourne True lorsque la pile est vide, False sinon."""
        return len(self.elements) == 0

    def __str__(self) -> str:
        return f"Pile : {self.elements}"

if __name__ == "__main__":
    # File d'attente pour un film
    # Les éléments sont des nomrbes entiers
    calcul = Pile[int]()
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
    
