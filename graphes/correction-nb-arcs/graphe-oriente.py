import copy

class GrapheOriente():
    def __init__(self, donnees):
        self.liste = copy.deepcopy(donnees)

    def nb_arc(self):
        nb = 0
        for e in self.liste.values():
            nb += len(e)
        return nb

lst_adj = {
    0 : [1, 4],
    1 : [5],
    2 : [0, 3, 5],
    3 : [1, 2],
    4 : [1, 2, 5],
    5 : [3]
}

go = GrapheOriente(lst_adj)
print(go.nb_arc()) # 12
