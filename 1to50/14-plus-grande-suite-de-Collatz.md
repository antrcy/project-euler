**Problème 14**

_La suite de Collatz est définie comme suite :_

$$
\begin{align*}
&n \to n/2 \text{ si $n$ est pair} \\
&n \to 3n+1 \text{ si $n$ est impair}
\end{align*}
$$

_En démarrant à $13$ par exemple, on obtient la séquence suivante :_

$$
13 \to 40 \to 20 \to 10 \to 5 \to 16 \to 8 \to 4 \to 2 \to 1
$$

_A partir de $1$ la suite alterne entre $1$, $4$, et $2$. On considèrera que la suite est achevée si elle atteint $1$. Il est conjecturé que toutes suites de Collatez s'achèvent en $1$. Déterminer la plus grande suite de Collatez avec condition initiale une valeur inférieure à 1 milion._ 

___

On pourrait créer une liste à 1 milion d'éléments qui indique pour chaque position initiale (l'indice) la taille de la suite de Collatz. En construisant cette liste itérativement on économise des comparaisons. Une particularité de la suite de Collatz est que l'on ne repasse jamais par la même valeur.