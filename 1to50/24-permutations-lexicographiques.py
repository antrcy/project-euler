def factorial(n):
    if n==0:
        return 1
    else:
        res = 1
        for i in range(1, n+1):
            res*=i
        return res


def nth_lexico_perm(k, tab):
    val = tab.copy()
    n = len(val)-1
    res = []
    r = k

    for _ in range(n):
        c = r//factorial(n)
        r = r%factorial(n)
        res.append(val[c])
        n-=1; val.remove(val[c])

    res.append(val[0])

    return res

answer=nth_lexico_perm(999_999, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
answer=sum(answer[9-i]*(10**i) for i in range(10))
print(f"Problème 24 : {answer}")
