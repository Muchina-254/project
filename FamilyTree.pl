% Facts
father(kimani, Kamau).
father(Kamau, ng'ang'a).
father(kamau, mwangi).
father(ng'ang'a, muchina).
father(ng'ang'a, wangui).
father(ng'ang'a, nduta).
father(ng'ang'a, wakanyi).
father(muchina, sarah).
father(muchina, anne).
father(muchina, susan).
father(muchina, samuel).
father(muchina, james).
father(muchina, david).


mother(njambi, muchina).
mother(nyambura, njeri).
mother(njeri, sarah).
mother(njeri, anne).
mother(njeri, susan).
mother(njeri, samuel).
mother(njeri, james).
mother(njeri, david).

% Rules
parent(X, Y) :- father(X, Y).
parent(X, Y) :- mother(X, Y).

siblings(X, Y) :- parent(Z, X), parent(Z, Y), X \= Y.

% Query examples
% Query: mother(X, sarah).
% Result: X = njeri.
%
% Query: siblings(X, samuel).
% Result: X = sarah ; X = susan ; X = anne ; X = james ; X = david.
