def nb_diviseurs(n):
    d = []
    div = 2
    n_copy = n

    while n_copy!=1:
        while n_copy%div!=0:
            div+=1
        d.append(0)
        while n_copy%div==0:
            n_copy//=div
            d[-1]+=1
    
    res = 1
    for i in d:
        res*=(i+1)
    return res

answer = 1
while nb_diviseurs(answer*(answer+1)//2)<500:
    answer+=1

# On peut améliorer notre réponse en précalculant une table de premiers

#print(f"Problème 12 : {answer}")