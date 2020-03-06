def ricercaBinaria(v,x,i,j):#vettore,x=valore da cercare, punto iniziale, punto finale
    if i>j:
        return False
    if i==j:
        return v[i]==x
    y=v[(i+j)//2]
    if x==y:
        return True
    if x<y:
        return ricercaBinaria(v,x,i,(i+j)//2-1)
    return ricercaBinaria(v,x,(i+j)//2+1,j)

def ricBinIterativa(v,x):
    i=0
    j=(len(v)-1)
    while(i<=j):
        r=(i+j)//2
        if(v[r]==x):
            return x
        if(v[r]<x):
            i=r+1
        else:
            j=r-1
    return None

A=[1,2,3,4,5,6,7,8,9]
print(ricercaBinaria(A,3,0,len(A)-1))
print(ricercaBinaria(A,5,0,len(A)-1))
print(ricBinIterativa(A,4))
        
