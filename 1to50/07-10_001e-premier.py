import math

n = 10_001
bound = int(n*math.log(n)+n*math.log(math.log(n)))

def crible(max):
    primes = (max+1)*[1]
    primes[0] = primes[1] = 0

    for k in range(2, int(math.sqrt(max))+1):
        for mul in range(2, max//k+1):
            primes[mul*k] = 0
    return [i for i in range(len(primes)) if int(primes[i])==1]

answer = crible(bound)[10_000]
#print(f"Problème 7 : {answer}")