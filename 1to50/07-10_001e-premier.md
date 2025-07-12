**Problème 7**

_Les six premiers nombres premiers sont :_

$$
2, 3, 5, 7, 11, 13
$$

_Déterminer le $10 001^{\text{ème}}$ premier._

___

On va utiliser le théorème des nombres premiers :

$$
p_n < n\ln(n) + n\ln(\ln(n))
$$

On obtient donc tous les premiers jusqu'à cette borne, et pour cela on utilise le crible d'Erathostène.