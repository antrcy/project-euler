def smallest(n):
    k = 2
    while (n%k!=0):
        k+=1
    return k

def largest_prime(n):
    m = n
    d = smallest(m)
    while m//d!=1:
        m//=d
        d=smallest(m)
    return d

answer=largest_prime(600851475143)
#print(f"Problème 3 : {answer}")