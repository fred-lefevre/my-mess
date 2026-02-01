
# Graphe oriente de 4 sommets et 4 arcs, mais trop de sommets
ko_1 = """GRAPHE ORIENTE
4 SOMMETS
Aurora
Ilona
Erik
Olavi
Tapio
4 ARCS
Aurora Olavi
Olavi Tapio
Tapio Olavi
Aurora Tapio
"""

# Graphe oriente de 4 sommets et 4 arcs, mais pas assez d'arcs
ko_2 = """GRAPHE ORIENTE
4 SOMMETS
Aurora
Ilona
Erik
Olavi
Tapio
4 ARCS
Aurora Olavi
Tapio Olavi
Aurora Tapio
"""

# Graphe non oriente de 4 sommets et 2 arêtes, mais le mot clé ARETE n'a pas de SA au début
ko_3 = """GRAPHE NON ORIENTE
4 SOMMETS
Aurora
Ilona
Erik
Olga
2 RETES
Erik Ilona
Aurora Olga
"""

# Graphe oriente, mais le mot clé ARETES et utilis au lieu du mot clé ARCS
ko_4 = """GRAPHE ORIENTE
4 SOMMETS
Aurora
Ilona
Erik
Olga
2 ARETES
Erik Ilona
Aurora Olga
"""

# Graphe non oriente de 4 sommets et 2 arêtes, mais la première ligne ne contient pas GRAPHE NON ORIENTE
ko_5 = """
GRAPHE NON ORIENTE
4 SOMMETS
Aurora
Ilona
Erik
Olga
2 ARETES
Erik Ilona
Aurora Olga
"""