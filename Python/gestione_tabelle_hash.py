def hashincr(n, h, j):
    return (h+j) %n

def hashinsert(tab,x):
    h=hash(x)%n
    i=h
    for j in range(1,n):
        if tab[i] == x:
            return True
        if tab[i] == "":
            tab[i]=x
            return True
        i=hashincr(n,h,j)
    return False

def hashsearch(tab,x):
    h=hash(x)%n
    i=h
    for j in range(1,n):
        if tab[i] == x:
            return True
        if tab[i] == "":
            return False
        i=hashincr(n,h,j)
    return False

def cerca(tab,x):
    if hashsearch(tab,x):
        print(x, " c'è")
    else:
        print(x, " non c'è")


n=13
A=n*[""]
hashinsert(A, "pippi")
hashinsert(A, "pluto")
hashinsert(A, "minnie")
hashinsert(A, "topolino")
hashinsert(A, "pippo")
hashinsert(A, "qui")
hashinsert(A, "quo")
hashinsert(A, "qua")
print("tabella ",A)
cerca(A,"qui")
cerca(A,"gambadilegno")

#Per evitare un agglomerato di chiavi cioè chiavi che si sovrappongono si può usare la scansione quadratica
def hashincr(n,h,i,j):
    return (h+j**2)%n
#Anche qui si possono avere agglomerati di chiavi quindi per ridurre ancora queste collisioni si usa
#La scansione quadratica a coefficienti pesati
def hashincr(n,h,i,j):
    return (h+w*j**2)%n



              
        
