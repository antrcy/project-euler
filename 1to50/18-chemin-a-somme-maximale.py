with open("files/pb18.txt", "r") as file:
    data = file.read()

data = data.split('\n')
data = [d.split(' ') for d in data]
data = [[int(k) for k in l] for l in data]
scores = data.copy()

n = len(scores)

def max2(x, y):
    return x*(x>y)+y*(y>=x)

for j in range(1, n):
    for k in range(n - j):
        l0 = scores[n-j-1]
        lm1 = scores[n-j]

        l0[k]+=max2(lm1[k], lm1[k+1])

answer = scores[0][0]
#print(f"Problème 18 : {answer}")