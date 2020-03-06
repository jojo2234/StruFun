def bolle(v): #Complessità n^2
    for i in range(n):
        for j in range(1,n-i):
            if v[j-1]>v[j]:
                scambia(v,j,j-1)
                
def selezione(v): #Complessità n^2
    for i in range(n-1):
        min=v[i]
        k=i
        for j in range(i+1,n):
            if v[j]<min:
                min=v[j]
                k=j
            if k!=i: #significa che v[j] è minore del minimo
                scambia(v,i,k)

def merge(v,l,c,r):
    i=k=1
    j=c+1
    while i<=c and j<=r:
        if v[i]<=v[j]:
            temp[k]=v[i]
            i=i+1
        else:
            temp[k]=v[j]
            j=j+1
        k=k+1
    while i<=c:
        temp[k]=v[i]
        i=i+1
        k=k+1
    while j<=r:
        temp[k]=v[j]
        j=j+1
        k=k+1
    for k in range(l,r+1):
        v[k]=temp[k]

def mergesort(v,l,r): #Complessità media n*log(n)
    if l>=r:
        return
    mergesort(v,l,(l+r)//2)
    mergesort(v,(l+r)//2+1,r)
    merge(v,l,(l+r)//2,r)

def quicksort(v,l,r):#media n*log(n) peggiore n^2
    if l>=r:
        return
    i=l
    j=r
    x=v[(l+r)//2]#Elemento (perno) casuale scelto sempre nel mezzo del prof
    while i<j:
        while x>v[i]:
            i=i+1
        while v[j]>x:
            j=j-1
        if i<=j:
            scambia(v,i,j)
            i=i+1
            j=j-1
        if l<j:
            quicksort(v,l,j)
        if i<r:
            quicksort(v,i,r)
    #Quando esce dal ciclo il progrmma termina

def heapsort(v):
    heapcostr(v)
    for i in range(1,n):
        scambia(v,0,n-i)
        heapricostr(v,0,n-1)

