res = 2
max_len = 0
for k in range(2, 1_001):
    c = 0
    Rs = [0]*(k+1)
    i = 1; d = 10; r = d%k
    while True:
        c+=1
        if Rs[r]!=0:
            c-=Rs[r]
            break
        Rs[r]=i
        d=r*10
        r=d%k
        i+=1
    if c>=max_len:
        max_len=c
        res=k

answer=max_len
print(f"Problème 26 : {answer}")