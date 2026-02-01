from typing import TypeVar, Generic

# Tous les éléments de la file seront d'un même type T.
T = TypeVar('T')

class File(Generic[T]):
    def __init__(self) -> None:
        # Initialise une liste d'éléments de type T
        self.elements: list[T] = []

    def enfiler(self, e: T) -> None:
        """Ajoute l'élément e à la fin de la file."""
        self.elements.append(e)

    def defiler(self) -> T:
        """
        Retire et renvoie le premier élément (T).
        Lève une exception si la file vide.
        """
        if self.est_vide():
            raise Exception("Impossible de retirer un élément d'une file vide")
        return self.elements.pop(0)

    def est_vide(self) -> bool:
        """Retourne True lorsque la file est vide, False sinon."""
        return len(self.elements) == 0

    def __str__(self) -> str:
        return f"File : {self.elements}"

if __name__ == "__main__":
    # File d'attente pour un film
    # Les éléments sont des prénoms (str)
    film = File[str]()
    print(film)
    film.enfiler("Bobby")
    film.enfiler("Ada")
    film.enfiler("Helmi")
    print(film)
    p = film.defiler()
    print(f"{p} vient de sortir de la file")
    print(film)
    print(f"La file est vide ? {film.est_vide()}")
    p = film.defiler()
    print(film)
    p = film.defiler()
    print(film)
    print(f"La file est vide ? {film.est_vide()}")
    
