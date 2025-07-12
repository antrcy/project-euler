with open("files/pb08.txt", "r") as file:
    data = file.read()

data = data.replace('\n', '')

def prod(s):
    res=1
    for i in range(len(s)):
        res*=int(s[i])
    return res


x=1; res=0; i=0
while i<=len(data)-13:
    k = data[i:i+13].find('0')
    if k>0:
        i=k+i+1
    else:
        d=prod(data[i:i+13])
        if d>x:
            x=d
            res=i
        i+=1

answer = prod(data[res:res+13])
#print(f"Problème 8 : {answer}")