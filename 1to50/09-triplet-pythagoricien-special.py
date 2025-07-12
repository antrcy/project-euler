n=1_000
for c in range(n//3, n//2):
    for b in range((n-c)//2, c):
        a = n-b-c
        if a**2 + b**2 == c**2:
            break
    else:
        continue
    break

answer=a*b*c
#print(f"Problème 9 : {answer}")