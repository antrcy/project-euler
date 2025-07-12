def february(n: int) -> int :
    if n%4!=0 or (n%100==0 and n%400!=0):
        return 28
    else:
        return 29

n = 1; answer = 0
for y in range(1901, 2001):
    years = [31,]+[february(y),]+[31,30,31,30,31,31,30,31,30,31]
    for m in years:
        n=(n+m)%7
        answer+=int(n==6)

#print(f"Problème 19 : {answer}")