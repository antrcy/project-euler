# Fibonacci récursif
def fibonacci_recursif(n):
    if n == 1:
        return 2
    if n == 0:
        return 1
    return fibonacci_recursif(n-1) + fibonacci_recursif(n-2)

# Fibonacci itératif
def fibonacci_iteratif(n):
    if n==1:
        return 2
    if n==0:
        return 1
    f1 = 2; f0 = 1
    f2 = f1 + f0
    for i in range(2, n):
        f1, f0 = f2, f1
        f2 = f1 + f0
    return f2

fibo = [2, 8]
while fibo[-1]<4_000_000:
    fibo.append(4*fibo[-1]+fibo[-2])

answer=sum(fibo[:-1])
#print(f"Problème 2 : {answer}")
