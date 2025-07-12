n = 20
answer = 1

for i in range(n+1, 2*n+1):
    k = i
    if k%2==0:
        k = 2
    answer*=k

for j in range(2,n//2+1):
    answer//=j

#print(f"Problème 15 : {answer}")