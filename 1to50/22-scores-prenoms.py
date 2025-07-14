with open("files/pb22.txt", "r") as file:
    names = file.read()

names = [name[1:-1] for name in names.split(',')]
alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

dico = {}
for k in range(len(alphabet)):
    dico[alphabet[k]]=k+1

name_num = []
for name in names:
    res = [dico[name[i]] for i in range(len(name))]
    name_num.append(res)

def A_before_B(A: list, B: list):
    k = 0
    while k<min(len(A), len(B)):
        if A[k]>B[k]:
            return False
        elif A[k]<B[k]:
            return True
        k+=1
    if len(A)>len(B):
        return False
    else:
        return True


max_len = max(len(n) for n in name_num)
ordered = []

while len(name_num)>0:
    n = name_num[0]
    for name in name_num[1:]:
        if A_before_B(name, n):
            n = name
    ordered.append(n); name_num.remove(n)


scores = [sum(ordered[i])*(i+1) for i in range(len(ordered))]

#print(f"Problème 22 : {sum(scores)}")