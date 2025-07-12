def is_pal(n):
    return str(n)==str(n)[::-1]

pal = []
for i in range(100, 1000):
    for j in range(110, 1000, 11):
        if is_pal(i*j):
            pal.append(i*j)

answer=max(pal)
#print(f"Problème 4 : {answer}")