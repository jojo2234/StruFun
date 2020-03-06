def nodo(x,s,d):
    return [x,s,d]

def foglia(x):
    return [x,None,None]

def vuoto():
    return None

def radice(A):
    return A[0]

def sinistro(A):
    return A[1]

def destro(A):
    return A[2]

def isVuoto(A):
    return A is None

def isFoglia(A):
    return isVuoto(sinistro(A)) and isVuoto(destro(A))

def isVuotoMIO(x):
    if x is None:
        return True
    if len(x)==0:
        return True
    if len(x)>0:
        return False

def radiceMIA(x):
    if isVuoto(x) is False:
        return x[0]
    else:
        return None

def sinistroMIO(x):
    #Implementare destro e sinistro (senza oggetti?!)
    return None

def destroMIO(x):
    #Implementare destro e sinistro (senza oggetti?!)
    #Con le liste
    return None

def fogliaMIA(x):
    #Così ritorna la prima foglia sulla sinistra che trova
    if sinistro(x) is None and destro(x) is None:
        return radice(x)
    elif destro(x) not is None:
        return foglia(sinistro(x))
    else return foglia(destro(x))
    
def ricerca(x,A):
    if isVuoto(A):
        return False
    if x==radice(A):
        return True
    if x<radice(A):
        return ricerca(x,sinistro(A))
    return ricerca(x,destro(A))

def inserzione(x,A):
    if isVuoto(A):
        return forglia(x)
    if x<radice(A):
        return nodo(radice(A),destro(A), inserzione(x,sinistro(A)))
    return nodo(radice(A), inserzione(x,destro(A)),sinistro(A))

#Solo per albero binario di ricerca pesato
def massimo(A):
    #Dove i figli a destra sono più pesanti(grandi) di quelli a sinistra
    #Quindi il massimo è il primo nodo senza figli destri che s'incontra scendendo
    #sempre a destra a partire dalla radice
    if isVuoto(destro(A)):
        return radice(A)
    return massimo(destro(A))

def scambia(a,i,j):
    if i!=j:
        a[i], a[j] = a[j], a[i]

#La roba da qui in poi vale solo per alberi HEAP (dove la radice e maggiore di entrambi i suoi figli e i nodi dell'ultimo livello sono tutti addossati a sinistra)
def padre(i):
    return (i-1)//2

def primofiglio(i):
    return 2*(i+1)-1

def heaptest(h,i):
    if i==0:
        return True
    return h[i] <= h[padre(i)]

def heapinser(h,x):#si inserisce il valore nella prima posizione libera se questo valore è minore del padre allora l'albero è ancora uno heap, altrimenti risale ricorsivamente verso la radice scambiando l'elemento con il padre
    h.append(x)
    i=len(h)-1
    while not heaptest(h,i):
        scambia(h,i,padre(i))
        i=padre(i)

def heapricostr(h,i,j):#Porta a heap un array già esistente
    #Da notare che heapricostr viene chiamato forse infinite volte quindi finisce?
    f1=primoFiglio(i)
    f2=f1+1
    if f1<j:
        k=f1
        if f2<j:
            if h[f2]>h[f1]:
                k=f2
        if not heaptest(h,k):
            scambia(h,k,padre(k))
            heapricostr(h,k,j)

def heapcostr(h):#per riorganizzare a heap un array di n elementi già allocato
    for i in range(len(h)-1, -1, -1):
        heapricostr(h,i,len(h))

def heapmassimo(h):#estrazione di un massimo da un heap
    max, h[0] = h[0], h.pop()
    heapricostr(h,0,len(h))


                    
                    
            
