#Esercizio: Scrivere un programma in Python che calcola il triangolo di tartaglia
#def tartaglia(stop):
#    if(stop < 0):
#        return 1
#    return tartaglia(stop-1)+stop
#print(tartaglia(5))
#Per trovare i numeri di fibonacci bisogna sommare i numeri del triangolo di tartaglia in diagonale, il primo è 1 il secondo è 1 il terzo è 2 da 1+1 e così via:

#                                 1 1 2 3 Seguendo le diagonali immaginarie si vede che il primo 1 risulta 1 il secondo 1 a sinistra non ha nessuno che copra la sua diagonale a destra e quindi 1+0=1 poi 1+1=2 e in diagonale 1+2=3
#                                1  
#                               1 1 
#                              1 2 1
#                             1 3 3 1
#                            1 4 6 4 1
#                          1 5 10 10 5 1
#Adesso funziona!!!
def generaTriangolo(stop):
    #stop è la linea di arresto
    v = [0]*(stop+1) #come si definisce un vettore?così va bene
    v[0] = 1
    for i in range(0,stop): #Per tutte le posizioni del vettore se i è 0 ci metto uno altrimenti faccio ogni volta la copia del vettore effettuo un ciclo for da 1 a i+1 e se tempVet[c]!=0 stampo il contenuto poi aumento c di 1
        if(i==0):
            v[i+1] = 1
            print(v[i])
        else:
            #print("Sono temp: ")
            tempVet = v[:] #Prima senza saperlo facevo alias cioè una copia ad indirizzo tempVet=v se modifico v modifico anche tempVet, ma con v[:] prendo una porzione di tutto il vettore effettuando una clonazione
            #print(tempVet)
            c=0
            for j in range(1,(i+1)):#poi assegno a v[j] (v[1]) il valore di tempVet[j-1] (quindi 1 per il primo ciclo) + tempVet[j] (zero per il primo ciclo) quindi v[j] prende 1 e il secondo valore in v[j] è 1 e assegno al valore successivo
                #parlo di v[i+1] un 1 come nel triangolo di tartaglia poi stampo tempVet[c] (che era incrementato di 1)e quindi ottengo una vera porcheria che però funziona.
                if(tempVet[c]!=0):
                    print(tempVet[c], sep=' ', end=" ", flush=True)
                    c = c+1
                #print("TEMPdiJ_PRIMA: " + str(tempVet[j]))
                v[j] = tempVet[j-1] + tempVet[j] #ci credo che non fa, tempVet[j] viene incrementato senza motivo di 1 dopo la somma col suo precedente Il motivo era il cosidetto alias
                #print("TEMPdiJ_DOPO: " + str(tempVet[j]))
                #print("v[j]["+str(j)+"] prende " + "tempVet[j-1]["+str(j-1)+"]=" + str(tempVet[j-1]) + " + tempVet[j]["+str(j)+"]="+str(tempVet[j]) + " => v[j]: " + str(v[j]))
            v[i+1] = 1
            print(tempVet[c], sep=' ', end=" ", flush=True)
            c=0
            #print("Sono V: ")
            #print(v)
            print()
print(generaTriangolo(15))
#def tartaglia(n,k):
 #   if n<1 or k<1:
  #      return 1;
   # return 7
#print (tartaglia(1,3))
#Nel triangolo di tartaglia si vede che le righe dispari hanno un valore centrale
#Il valore centrale forse viene generato seguendo una qualche regola che non richiede che venga calcolato tutto il triangolo
#I valori centrali a me conosciuti sono: 1,2,6,20,70..
#Visto che n corrisponde alla riga del triangolo e k alla posizione sapendo che i valori centrali sopra esposti sono la riga dispari si potrebbe trovare tutti i valori vicini partendo da quello centrale più vicino
#ad n senza calcolare tutto il triangolo di tartaglia, per esempio con n=4 basta sommarvi 1 spostandoci quindi sulla linea dispari numerata come quinta, su questa linea sappiamo esserci il 6 perchè 1 è alla prima linea, la seconda si
#salta sulla terza c'è il 2 e la quarta si salta e sulla 5 c'è il 6, quindi bisogna ottenere una formula per ottenere da n la posizione nel vettore in cui beccare il valore, esempio 5-2 = 3 in 3 posizione abbiamo il 6 la formula
#corrisponde a se (n+1) è dispari faccio(n+1)//2 altrimenti n//2, ottenendo la posizione del vettore in cui c'è il valore centrale del triangolo comunque questo non ci permette di ottenere tutti i valori centrali del triangolo
#Nel triangolo di tartaglia si nota che ci sono anche i numeri primi
