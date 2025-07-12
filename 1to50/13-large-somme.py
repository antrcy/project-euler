with open("files/pb13.txt", "r") as file:
    data = file.read()

num=data.replace('\n', ' ').split(' ')
num=[n[::-1] for n in num]

res = []
r = 0

for d in range(50):
    s = r
    for n in num:
        s+=int(n[d])
    r = s//10
    res.append(s%10)
while r!=0:
    res.append(r%10)
    r = r//10

res=res[::-1][0:10]

answer=0
for n in range(10):
    answer+=(res[9-n]*10**n)

#print(f"Problème 13 : {answer}")