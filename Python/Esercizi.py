#Es.1 Dato un array contenente solo 0 e 1 fare un programma che lo ordina in tempo lineare senza usar array o liste di appoggio
def ordina(A):
    v0=0
    for i in range(len(A)):
        if A[i]==0:
            v0=(v0+1)
    print("v0: " + str(v0))
    for j in range(0,v0):
        A[j]=0
    start = (v0)
    stop = (len(A))
    for x in range(start,stop):
        A[x]=1
    return A

vet = [0,1,0,1,0,1,1,1,0,0,0,1,0,1]
print(ordina(vet))

#Es.2 Scrivere un programma che dato un array A contenente solo i valori -1 35 e 27685, lo ordina in tempo lineare senza usare array o liste di appoggio
def ordina2(A):
    v1=0
    v2=0
    for i in range(len(A)):
        if A[i]==-1:
            v1=v1+1
        if A[i]==35:
            v2=v2+1
    for j in range(v1):
        A[j]=-1
    for j in range(v1,(v1+v2)):
        A[j]=35
    for j in range((v2+v1),len(A)):
        A[j]=27685
    return A

vet = [35,35,-1,27685,35,27685,-1,-1,-1,27685,35,-1,35,35]
print(ordina2(vet))

#Es.3 Dare un programma che dato un array A contenente interi compresi tra 0 e m-1 con m<len(A) lo ordina in tempo lineare

def scambia(v,i,j):
        if i!=j:
            v[i],v[j]=v[j],v[i]

def quicksort(v,l,r):#media n*log(n) peggiore n^2
    if l>=r:
        return
    i=l
    j=r
    x=v[(l+r)//2]#Elemento (perno) casuale scelto sempre nel mezzo dal prof
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

def ordina3(A,m):
    quicksort(A,0,(len(A)-1)) #Col quicksort non è in tempo lineare ma O(n*log(n)) PERò non è la complessità il tempo lineare quindi va bene.
    return A
        #Si possono usare array o liste di appoggio conviene dunque usare un algoritmo di ordinamento crescente e quindi il quicksort è il migliore per ora
def ordina3_2(A,m):
    v=[0]*m #Si instanzia un vettore di 0 lungo quanto il massimo degli elementi dentro al vettore A (m-1), che guarda caso equivale alla lunghezza di A.
    for a in A:#Si scorre A è ogni volta che ad esempio compare un 5 si va in posizione 5 del vettore v e si mette un +1 così facendo si sa quante occorrenze di numeri ci sono in A.
        v[a]=v[a]+1 #v è un vettore di zeri
        #praticamente usando il valore in a come indirizzo se si presenta un altro valore simile lo stesso indirizzo viene incrementato di uno, quindi così si sa quanti di quel numero ci sono tanto m<len(A)
    k=0 #A questo punto basta fare 2 cicli e si riempe il vettore delle varie occorrenze che ci sono in A scorrendo per m e incrementando k per quanti v[i] con quel numero ci sono.
    for i in range(m):# in questo caso for da 0 a 10
        for j in range(v[i]):# per il primo ciclo e un for di 1 perchè v[0]=1 c'è un solo 0 nel vettore ma per il settimo v[7]=2 c'è 2 sette nel vettore
            A[k]=i #Poi ad A[k] con k che parte da 0 gli assegno i che sono i valori dell'array e lo ordino in tempo lineare
            k=k+1 #k è l'indice di A
    return A

vet=[0,3,6,2,7,5,9,4,1,8,7]#vet viene ridefinito

print(ordina3(vet,10))
print(ordina3_2(vet,10))

#Es.4 Dare un programma che dato un array A di numeri restituisce la somma di quelli di posto pari
def sommaPostoPari(A):
    s=0
    for i in range(0,len(A)):
        if i%2==0:
            s=s+A[i]
    return s

def sommaPostoPari2(A):
    s=0
    for i in range(0,len(A),2):
        s=s+A[i]
    return s

print("sommaPari1: " + str(sommaPostoPari(vet)))
print("sommaPari2: " + str(sommaPostoPari2(vet)))

#Es.5 Dare un programma che dato un array A di numeri interi restituisce la somma di quelli di valore pari
def sommaNumPari(A):
    s=0
    for i in range(0,len(A)):
        if A[i]%2==0:
            s=s+A[i]
    return s

print(sommaNumPari(vet))

#Es.6 Dare un programma che dato un array A ordinato contenente numeri interi determina in tempo lineare credo con O(n) se vi sono due elementi la cui somma è k
def sommaK(A,k):
    #Controllo se la somma del primo e del ultimo elemento del vettore ordinato è uguale a k se non lo è guardo se k è maggiore della somma ciò significa che per trovare k devo sommare numeri più grandi quindi incremento i
    i=0
    j=len(A)-1
    while i<j:
        if A[i]+A[j] == k:
            return True
        if k>(A[i]+A[j]):
            i+=1
        else:#k<(A[i]+A[j])
            j-=1
    return False

vet=[3,5,8,12,14,17,16,22,24]
print(sommaK(vet,15))

#Es.7 Scrivere un programma che accetta in input due array ordinati di uguale lunghezza n contenenti interi distinti e restituisce in output il numero di elementi che occorrono in entrambi gli array. La complessità deve essere lineare.
def ordinati(A,B):
    i=0
    j=0
    n=0
    while i<len(A) and j<len(B):
        if A[i]==B[j]:
            n+=1
            i+=1
            j+=1
        elif A[i]<B[j]:
            i+=1
        else:
            j+=1
    return n
v1=[3,6,7,8,9,12]
v2=[0,1,2,3,4,9]
print(ordinati(v1,v2))

#Es.8 Scrivere due programmi uno encode(A) che riceve in input un array contenente gli elementi di A a partire dalla posizione 0 e restituisce un array B contenenti gli elementi di B a partire dalla posizione 0 e uno decode(B)
#che riceve in input un array B contenente gli elemneti di B a partire dalla posizione 0 e rende un array A contenente gli elementi di A a partire dalla posizione 0
def encodeMIO(A):
    B = A[:]
    return B
def encode(A):
    B=[0]*A[-1]#istanzio un vettore B di zeri lungo quanto A
    for x in A:
        #Quindi x è l'elemento di A[i]
        B[x-1]=B[x-1]+1#Quindi come l'es 3 uso il valore in A[i] come indirizzo e sommo le occorrenze
    return B
#Così da poter decodificare l'array anche senza avere A ottengo un array A ordinato in tempo lineare.
def decode(B):
    m=0
    for x in B: #per la lunghezza di B somma x ad m ottenendo quindi la lunghezza originaria di A
        m=m+x
    A=[0]*m#Esempio se B è lungo 5 ed è così B=[1,1,3,2,1] A viene lungo 8 perchè m somma i valori interni a B
    k=0
    for i in range(len(B)): #Poi scorro di 5 l'array e ogni volta scorro il suo valore quindi m ha senso
        for j in range(B[i]):
            A[k]=i+1
            k=k+1
    return A

#A=[5,2,3,5,2,2,7,8]#Infatti in posizione x-1 cioè 4 per il primo ciclo di encode ci finirà il valore 2 mentre in 2 posizione il 3 un pò come una tabella dove all'indirizzo di quel valore vengono sommate le occorrenze
#Le posizioni che non vengono toccate restano a zero perciò in decode mi creo un vettore che sembra essere per forza lungo quanto era A all'inizio
A=[1,1,1,2,3,3,5,6,7]# Infatti non mi tornava con i valori del prof per pura coincidenza sarà perchè sono ordinati torna tutto lo codifica e lo decodifica correttamente ma con i miei no
#A=[2,6,3,7,9,9,9,9,7,3] Infatti è necessario come per l'es 3 che i vettori siano ordinati anche se non era specificato in modo esplicito nell'esercizio
print(A)
B=encode(A)
print(B)
C=decode(B)
print(C)
    
#Es.9 scrivere un programma solomon(m) che rende un array A, di lunghezza m+1, contenente i primi m elementi della sequenza di Solomon Golomb a partire dalla posizione 1
#Non ho capito come viene generata questa sequenza di solomon quindi provo direttamente la soluzione:
def solomon(m):
    A=[0]*(m+1)
    A[0]=''
    A[1]=1
    A[2]=2
    h=2
    for i in range(2,m):
        for j in range(A[i]):
            if h>m:
                return A
            A[h]=i
            h=h+1
#Sembrerebbe che forse dalla posizione 2 in poi assegna il valore di per il numero di volte che c'è scritto in A[i] spostandosi ogni volta di una casella con la variabile h
#Perciò più il numero è grande più la sequenza cresce lentamente perchè ripete i soliti valori per tot volte finchè non arriva con i ad m ad esempio con 1560 iterazioni arriva fino a 113 mentre con 5560 fino a 248
print("Solomon" + str(solomon(10)))

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
        return forglia(x)#: il prof ha messo i due punti ma secondo me non ci vanno
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

def stampaAlbero(A):
    print(" ")
    stampaAlbero1(A," ")
    print(" ")

def stampaAlbero1(A,s):
    if not isVuoto(A):
        stampaAlbero1(destro(A),s+" ")
        print(s,radice(A))
        stampaAlbero1(sinistro(A),s+" ")
#Es.10 Scrivere un programma ricorsivo che dato un albero binario con valori numerici ai nodi calcola la somma degli elementi non foglia: QUINDI DI QUELLI CENTRALI
def sommaNodiC(A):
    if isFoglia(A) or isVuoto(A):
        return 0
    return radice(A)+sommaNodiC(sinistro(A))+sommaNodiC(destro(A))

D=nodo(8,foglia(9),foglia(2))
B=nodo(7,foglia(5),D)
C=nodo(12,foglia(6),foglia(4))
A=nodo(32,B,C)
#Albero:
#       32      Livello 0 è pari
#     7   12    Livello 1 è dispari
#    5 8 6  4   Livello 2 è pari
#     9 2       Figli di 8
stampaAlbero(A)
print("Somma nodi non foglia: " + str(sommaNodiC(A)))

#Es.11 Scrivere un programma ricorsivo che dato un albero binario con valori numerici ai nodi calcola la somma degli elementi al livello k:
def sommaLivello(A,k):
    #Quando k si azzerra siamo arrivati al livello k perciò viene fatta la somma di quei valori
    if isVuoto(A):
        return 0
    if k==0:#Ritorna la radice solo se il nuovo chiamante gli passa un k a zero
        #print("ROOT: " + str(radice(A)))
        return radice(A)#Questa funzione somma i numeri che stanno sullo stesso livello dell'albero
    return sommaLivello(sinistro(A),k-1)+sommaLivello(destro(A),k-1)
print("sommaLivello: " + str(sommaLivello(A,2)))

#Non è un es:
def visitaAnticipata(A):
    #radice,sinistro,destro
    if isVuoto(A):
        return 0
    print(radice(A))
    visitaAnticipata(sinistro(A))
    visitaAnticipata(destro(A))
    
#print(visitaAnticipata(A))

def visitaSimmetrica(A):
    if isVuoto(A):
        return None
    visitaSimmetrica(sinistro(A))
    print("-"+str(radice(A))+"-")
    visitaSimmetrica(destro(A))

#print(visitaSimmetrica(A))  
#Es.12 Scrivere un programma ricorsivo che dato un albero binario con valori numerici ai nodi calcola la somma degli elementi a distanza pari della radice:
def sommaP(A):
    if isVuoto(A):
        return 0
    #print("Radice(A): " +str(radice(A)))
    return radice(A)+sommaD(sinistro(A))+sommaD(destro(A))

def sommaD(A):
    if isVuoto(A):
        return 0
    return sommaP(sinistro(A))+sommaP(destro(A))

print("sommaDistanzaPari: " + str(sommaP(A)))
print("sommaDistanzaDispari: " + str(sommaD(A)))

#Es.14 Scrivere un programma ricorsivo che dato un albero binario con valori numerici positivi ai nodi calcola il massimo degli elementi a distanza pari dalla radice:
def maxP(A):
    if isVuoto(A):
        return 0
    return max(radice(A),maxD(sinistro(A)), maxD(destro(A)))
def maxD(A):
    if isVuoto(A):
        return 0
    return max(maxP(sinistro(A)),maxP(destro(A)))

print("Massimo numero a distanza pari dalla radice: " + str(maxP(A)))
#Es.13 Scrivere un programma ricorsivo che dato un albero binario con valori numerici positivi ai nodi calcola il massimo degli elementi a distanza dispari dalla radice.
print("Massimo numero a distanza dispari dalla radice: " + str(maxD(A)))
