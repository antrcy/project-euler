import math

# Plus efficace : un crible, mais ici ce n'est pas nécessaire
def is_prime(n):
    res = True
    for i in range(2, int(math.sqrt(n))+1):
        if n%i==0:
            return False
    return res

def primes(n):
    res = []
    for i in range(1,n+1):
        if is_prime(i):
            res.append(i)
    return res

p = primes(20)[1:]

answer = 1
for primes in p:
    k = primes
    while k<=20:
        k*=primes
    answer*=k//primes

#print(f"Problème 5 : {answer}")