**Problème 2**

_Chaque terme de la suite de Fibonacci est obtenu en sommant les deux précédents. Avec comme premiers termes $1$ et $2$, les $10$ premiers termes sont :_

$$
1, 2, 3, 5, 8, 13, 21, 34, 55, 89, \dots 
$$

_Déterminer la somme des termes pairs de la suite de Fibonacci inférieurs $4$ milions._

___

La suite de Fibonacci est définie par la relation de récurrence suivante :

$$
\begin{cases}
u_{n+2} = u_{n+1} + u_{n} \\
u_0 = 1, \quad u_1 = 2
\end{cases}
$$

On a donc :

$$
u_{n+2} = u_{n} + u_{n-1} + u_{n} = 2u_{n} + u_{n-1}
$$

Ainsi le terme $n+2$ est pair si et seulement si le terme $n-1$ l'est. On en déduit que tous les termes de la forme $u_{3k+1}$ sont pairs et que les termes de la forme $u_{3k}$ et $u_{3k+2}$ sont impairs, pour $k \in \mathbb{N}$. On établit la relation de récurrence suivante :

$$
\begin{cases}
    u_{3k+1} = 4 u_{3k-2} + u_{3k-5}, \quad \forall k \geq 2  \\
    u_1 = 2, u_4 = 8
\end{cases}
$$