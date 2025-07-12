**Problème 9**

_Un triplet Pythagoricien est un triplet d'entiers naturels $0 < a < b < c$ tels que :_

$$
a^2 + b^2 = c^2
$$

_Il existe un unique triplet Pythagoricien tel que $a + b + c = 1000$. Déterminer le produit $abc$._

___

Sans connaissance mathématique particulière, on peut déterminer des bornes de recherche :

$$
\begin{align*}
&(a + b)^2 = a^2 + b^2 + 2ab \\

&\iff (1000-c)^2 = c^2 + 2ab \\

&\implies c < 500
\end{align*}
$$

De plus :

$$
\begin{align*}
&1000 - b - c < b < c \\

&\iff 1000 < 2b + c < 2c + b \\

&\implies b \in \left(\frac{1000-c}{2}, c\right) \ c \in \left(\frac{1000}{3}, 500 \right)
\end{align*}
$$

Pour ce problème, et probablement d'autres, le gain de cette méthode par rapport à une approche plus "naïve" est probablement négligeable.