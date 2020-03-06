def pos(x):
    #Questa è una funzione biunivoca che associa alla chiave x un numero tra 0 e (2^k)-1
    #Tipicamente pos(x) è l'intero equivalente alla rappresentazione binaria dei byte di x
    #In questo esempio c'è una tabella di 2^16 valori booleani per memorizzare un insieme di numeri interi compresi tra 0 e 2^16
    return x & 0x0000ffff

def insert(a, x):
    a[pos(x)]=True

def search(a, x):
    return a[pos(x)]

tab = 2**16 * [False]
insert(tab,10)
insert(tab,100)
insert(tab,35)
print(tab)
print(100, search(tab, 100))
print(101, search(tab, 101))
