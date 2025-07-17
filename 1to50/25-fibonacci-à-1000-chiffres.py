import math

def count_digits_str(n):
    return len(str(n))

def count_digits_fast(n):
    return 1+math.log10(n)

answer=3
Fn = 2; Fnm1 = 1; Fnm2 = 1
while count_digits_fast(Fn)<1000:
    answer+=1
    Fnm1, Fnm2 = Fn, Fnm1
    Fn = Fnm1+Fnm2

#print(f"Problème 25 : {answer}")