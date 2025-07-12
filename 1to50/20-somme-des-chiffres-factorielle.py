def factorial(n):
    res = 1
    if n==0:
        return res
    else:
        for i in range(1,n):
            res *= i
    return res

n = factorial(100)

answer = 0
while n!=0:
    answer+=n%10
    n=n//10

#print(f"Problème 20 : {answer}")