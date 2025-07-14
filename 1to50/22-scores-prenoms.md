**Problème 22**

_On possède un fichier `pb22.txt` contenant plus de $5000$ prénoms. Commencer par ranger ces prénons dans l'ordre alphabétique. Calculer ensuite la somme des scores de tous les prénoms. Le score d'un prénom est calculé en sommant la position de chacune de ses lettres dans l'alphabet, puis en mutlitpliant le résultat par la position du prénom dans l'odre alphabétique._

_Exemple_ : `COLIN`

$$
(3 + 15 + 12 + 9 + 14) \times 938 = 53 \times 938
$$

___

La solution implémentée ne me satisfait pas entièrement. Un meilleur algorithme de tri pourrait être utilisé ou un tri type radix.