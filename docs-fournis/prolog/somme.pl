%% somme.pl

somme([E],E):-
    number(E).
somme([E|L],S):-
    number(E),
    somme(L,S1),
    S is E + S1.
