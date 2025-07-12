def get_factors(n: int) -> list :
    res = [1]
    k = 2
    max = n//2
    while k<=max:
        if n%k==0:
            res.append(k)
            if max!=k:
                res.append(max)
        k+=1
        max=n//k
    return res

def is_amicable(n: int) -> bool | int:
    s1 = sum(get_factors(n))
    s2 = sum(get_factors(s1))
    return n==s2, s1

answer=0
for i in range(1,10_001):
    b, s = is_amicable(i)
    if b and s!=i:
        answer+=i

#print(f"Problème 21 : {answer}")