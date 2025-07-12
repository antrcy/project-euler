**Problème 21**

_Soit $d(n)$ la somme des diviseurs propres de $n$. Si $d(a)=b$ et $d(b)=a$, avec $a \neq b$, alors $a$ et $b$ forment une paire amicale et $a$ et $b$ sont des nombres amicaux. On ne considère donc pas les nombres parfaits ici._

_Par exemple, les diviseurs propres de $220$ sont $1,2, 4, 5, 10, 11, 20, 22, 44, 55$ et $110$; ainsi, $d(220)=284$. Les diviseurs propres de $284$ sont $1, 2, 4, 71$ et $142$; donc $d(284)=220$._

_On demande de déterminer la somme des nombres amicaux inférieurs à $10000$._

___

La principale difficulté est de déterminer les diviseurs propres d'un entier efficacement. On peut faire ça en $O(\sqrt n)$.