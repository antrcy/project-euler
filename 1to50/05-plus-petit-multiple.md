**Problème 5**

$2520$ _est le plus petit nombre divisible par tous les entiers de $1$ à $10$. Déterminer le plus petit entier positif divisible par tous les nombres de $1$ à $20$._

___

On commence par déterminer tous les nombres premiers de $1$ à $20$ : $p_0, \dots, p_n$. Puisque que tous les facteurs premiers des entiers de $1$ à $20$ appartiennent à $\{ p_0, \dots, p_n \}$, il suffit de prendre $\prod_{k=0}^n p_k^{\lfloor \log_{p_k}(20) \rfloor }$.