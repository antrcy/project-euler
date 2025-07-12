with open("files/pb11.txt", "r") as file:
    data = file.read()

data=data.replace('\n', ' ').split(' ')[1:-1]
seq_num=[int(data[i]) for i in range(len(data))]
seq_num=[seq_num[i:i+20] for i in range(0,len(seq_num),20)]

maxi = 0
typ = ''
imaxi, jmaxi = 0, 0

def prod(vec: list) -> int:
    res = 1
    for i in range(len(vec)):
        res*=vec[i]
    return res

for l in range(len(seq_num)):
    for c in range(len(seq_num[l]) - 4):
        view = seq_num[l][c:c+4]
        if 0 in view:
            continue
        else:
            new = prod(view)
            if new>maxi:
                maxi=new
                imaxi, jmaxi = l, c
                typ = 'c'
        view = [seq_num[c+i][l] for i in range(4)]
        if 0 in view:
            continue
        else:
            new = prod(view)
            if new>maxi:
                maxi=new
                imaxi, jmaxi = c, l
                typ = 'l'
for l in range(len(seq_num)-4):
    for c in range(len(seq_num)-4):
        view = [seq_num[l+i][c+i] for i in range(4)]
        if 0 in view:
            continue
        else:
            new = prod(view)
            if new>maxi:
                maxi=new
                imaxi, jmaxi = l, c
                typ = 'd1'
        view = [seq_num[l+4-i][c+i] for i in range(4)]
        if 0 in view:
            continue
        else:
            new = prod(view)
            if new>maxi:
                maxi=new
                imaxi, jmaxi = l+4, c
                typ = 'd2'

imaxi, jmaxi, typ, maxi
answer = maxi
#print(f"Problème 11 : {answer}")