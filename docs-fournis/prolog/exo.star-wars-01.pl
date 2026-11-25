%% exo.star-wars-01.pl

% Les catégories
categorie(jedi,'Chevalier Jedi').
categorie(sith,'Seigneur noir des Sith').

% Les personnages
perso(1, 'Dark Maul').
perso(2, 'Jar Jar Binks').
perso(3, 'Obi-Wan Kenobi').
perso(4, 'Sheev Palpatine').

% Les principaux éléments de l'intrigue du film
principal('Étoile Noire').
principal('Obi-Wan Kenobi').
principal('Sheev Palpatine').

% avec_categorie(Per,Cat) signifie que le personnage Per appartient à la catégorie Cat
avec_categorie(4,sith).
avec_categorie(1,sith).
avec_categorie(3,jedi).

% Surnoms de certains personnages
surnom(4, 'Dark Sidious').
