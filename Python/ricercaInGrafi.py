from collections import deque
import heapq
grafo={0:[8], 1:[2], 2:[0], 3:[1,2,0], 4:[6,7], 5:[6,7], 6:[3,4], 7:[6,8], 8:[]}

visitati=[]

def goal(x):
    return x==0

def DFR(nodo):
    visitati.append(nodo) #Si appende in visitati il valore passato e si analizza il primo a cui è collegato
    if goal(nodo): #Si cerca lo zero
        return True
    for x in grafo[nodo]:
        if visitati.count(x) == 0:
            if DFR(x):
                return True
    return False

def DF(nodo): #Stesso algoritmo ma con pila
    p=[nodo]
    while len(p)>0:
        nodo=p.pop()
        if visitati.count(nodo)==0:
            visitati.append(nodo)
            if goal(nodo):
                return True
            for x in reversed(grafo[nodo]):#Cosa fa reserved?#Va be funziona come quello ricorsivo
                p.append(x)
    return False

def BF(nodo):#Stesso di sopra ma con una CODA
    q = deque([nodo])
    while len(q)>0:#Essendo in coda tira via il primo inserito quindi quando si passa il 5 quel foreach in fondo riempe solo con i nodi a cui è legato 5 cioè 6 e 7 poi torna su e puppa cioè prende il primo valore inserito quindi 6 e
        #inserisce con quel foreach i nodi a cui è collegato cioè 3 e 4 poi puppa il 7 il 3 scende in prima posizione il 4 in seconda e poi inserisce il 6 e l'8 a cui è collegato il nodo 7 per poi rieffettuare la stessa operazioe
        #con il 3 finchè non arriva a puppare lo zero allora si interrompe.
        nodo=q.popleft()
        if visitati.count(nodo)==0:
            visitati.append(nodo)
            if goal(nodo):
                return True
            for x in grafo[nodo]:
                q.append(x)
           # print("Questa è q: " + str(q))
    return False


#Qui viene usato un heap al posto della pila

def Euristica(nodo):
    pq=[]
    heapq.heappush(pq,nodo)
    while len(pq)>0:
        nodo=heapq.heappop(pq)#Questo algoritmo inserisce tutti nodi del grafo analizzato dentro un heap che viene come sotto_:
        #print("nodo: " + str(nodo))
        if visitati.count(nodo)==0:
            visitati.append(nodo)
            if goal(nodo):
                return True
            for x in grafo[nodo]:
                heapq.heappush(pq,x)
    return False

#HEAP: Forse è così
#        8
#       6 7
#      5 4
#     3 
#    2
#   1 0
#Così è senza ripetizioni anche se in teoria ci sono più inserimenti con numeri uguali

if DFR(5):
    print("DFR         Eureka ", visitati)
visitati = []
if DF(5):
    print("DF          Eureka ", visitati)
visitati = []
if BF(5):
    print("BF          Eureka ", visitati)
visitati = []
if Euristica(5):
    print("EU          Eureka ", visitati)
    


