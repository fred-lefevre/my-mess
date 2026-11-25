%% kb.famille-bovin.pl

vache(ada).
vache(tara).
vache(sveiney).
vache(johanna).
vache(helma).
vache(sofia).
vache(britt).
vache(solveig).
vache(uddi).
vache(arna).
vache(jara).

taureau(gunnar).
taureau(erik).
taureau(olaf).
taureau(bruno).
taureau(kristo).
taureau(valter).
taureau(soren).
taureau(hogni).
taureau(bjarn).
taureau(gustav).

parent(ada, tara).
parent(gunnar, tara).
parent(sveiney, olaf).
parent(erik, olaf).
parent(ada, johanna).
parent(kristo, johanna).
parent(valter, soren).
parent(valter, helma).
parent(valter, sofia).
parent(johanna, soren).
parent(johanna, helma).
parent(johanna, sofia).
parent(tara, hogni).
parent(olaf, hogni).
parent(tara, britt).
parent(olaf, britt).
parent(tara, bruno).
parent(erik, bjarn).
parent(erik, uddi).
parent(solveig, bjarn).
parent(solveig, uddi).
parent(bjarn, bruno).
parent(arna, jara).
parent(bruno, jara).
parent(arna, gustav).
parent(bruno, gustav).

% enfant(E, P) signifie que E est l'enfant du parent P
% E est l'enfant de P si P est le parent de E
enfant(E, P) :- parent(P, E).

