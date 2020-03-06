def somma1(v,i,j):#i=inizio del vettore, j=elemento da sommare
    print("somma1")
    if i==j:
        return v[i]
    else:
        return somma1(v,i,(i+j)//2)+somma1(v,(i+j)//2+1,j)
    #Credo che questa somma sia di complessità computazionale quadratica

def somma2(v,i,j):
    print("somma2")
    if i==j:
        return v[i] #questo qui lo fa n volte quindi è lineare come quello sotto
    return v[i]+somma2(v,i+1,j)

def somma3(v):
    print("somma3: " + str(len(v)))
    s=0
    for i in range(len(v)):
        s=s+v[i]
    return s

A=[0,1,2,3,4,5,6,7,8,9]
print(somma1(A,0,len(A)-1), somma2(A,0,len(A)-1), somma3(A))
