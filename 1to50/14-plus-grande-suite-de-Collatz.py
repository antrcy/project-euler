dico = {}
max = 1; imax=1

for i in range(2, 1_000_001):
    next = i
    temp = []
    c=2
    while next!=1:
        if dico.get(next)==None:
            temp.append(next)
            if next%2==0:
                next=next//2
            else:
                next=3*next+1
        else:
            c=dico.get(next)
            next=1
    for j in range(len(temp)):
        dico[temp[j]]=c+len(temp)-j
    if dico[i]>max:
        max=dico[i]
        imax=i

answer = imax
#print(f"Problème 14 : {answer}")