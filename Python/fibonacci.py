def fibRic(n): #Complessità esponenziale
    print(n)
    if n<=3:
        return 1
    return fibRic(n-1)+fibRic(n-2)

def fibIte(n): #Complessità lineare
    v=[0]*(n+1)
    v[1]=1
    for i in range(2,n):
        v[i]=v[i-1]+v[i-2]
    return v[n-1]

print(fibRic(9))
print(fibIte(9))

#fib[0,1,1,2,3,5,8,13,21,34]
#pos[1,2,3,4,5,6,7, 8, 9,10]
#per fibRic(n):
#con 8 richiama 25 volte se stessa
#con 14 richiama ? comunque più del suo quadrato
#con 9 richiama 41 volte
#cresce più lentamente del quadrato all'inizio ma poi cresce esponenzialmente

