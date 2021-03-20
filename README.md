# Langton-s-ant
A little project which present the display of Langton's ant

Ce projet a pour but d'afficher le cheminement emprunté par différentes fourmis dans une matrice.
La taille de la fenetre est indépendant du nombre de case. On peut la modifier à notre guise.
On peut également augmenter le nombre de ligne et de colonnes.

Pour rajouter des couleurs/types de fourmis, il est nécéssaire de modifier le fichier antType.txt qui se présente sous la forme suivante, par exemple:

red:DGGDG
blue:GGDDG
green:GGDDD
yellow:DGDGG

G et D correspondent à un comportement, respectivement aller à gauche et aller à droite. Il est important de noter que le comportement d’une fourmi quand elle rentre dans une case à sa couleur ne doit jamais être identique à celui d’une case vide. Le premier comportement est celui de la fourmi pour la case par défaut (blanche).

On est peut également modifier la fréquence de mise à jour de l'écran.
