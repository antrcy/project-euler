bound = 28_123

def sum_factors(n: int) -> list :
    res = 1
    k = 2
    max = n//2
    while k<=max:
        if n%k==0:
            res+=k
            if max!=k:
                res+=max
        k+=1
        max=n//k
    return res

def is_abondant(n):
    return sum_factors(n)>n

k = 12
coeff = []

while k<=bound:
    if is_abondant(k):
        coeff.append(k)
    k+=1

check = [False]*(bound+1)

for i in range(len(coeff)):
    for j in range(i, len(coeff)):
        s = coeff[i] + coeff[j]
        if s <= bound:
            check[s]=True
        else:
            break

answer=sum(i for i, v in enumerate(check) if not v)
print(f"Problème 23 : {answer}")