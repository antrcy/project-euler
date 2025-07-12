def mul_3_or_5(n):
    n1 = n//5-1; n2 = n//3; n3 = n2//5
    return (5*(n1*(n1+1))//2 + 
            3*(n2*(n2+1))//2 - 
            15*(n3*(n3+1))//2)

def mul_3_or_5_bis(n):
    k=3
    res=0
    while k<n:
        if (k%3==0 or k%5==0):
            res+=k
        k+=1
    return res

answer=mul_3_or_5(1_000)
#print(f"Problème 1 : {answer}")
