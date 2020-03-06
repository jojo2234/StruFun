def triangle(n): #ricorsiva in coda (fa uso del for non è pura)
    if n==0:
        return []
    elif n==1:
        return [[1]]
    else:
        new_row = [1]
        result = triangle(n-1)
        last_row = result[-1]
        for i in range(len(last_row)-1):
            new_row.append(last_row[i] + last_row[i+1])
        new_row +=[1]
        result.append(new_row)
    return result

def generaTriangolo(stop): #iterativa
    v = [0]*(stop+1)
    v[0] = 1
    for i in range(0,stop):
        if(i==0):
            v[i+1] = 1
            print(v[i])
        else:
            tempVet = v[:] #porzione del vettore in questo caso completa usata per clonare il vettore in tempVet solamente con l'assegnamento facevo un passaggio di indirizzo quindi finivo col modiicare lo stesso vettore
            c=0
            for j in range(1,(i+1)):
                if(tempVet[c]!=0):
                    print(tempVet[c], sep=' ', end=" ", flush=True)
                    c = c+1 #Questo incremento mi fa stampare il secondo 1 quando c!=0 o quando sono in cascata sequenziale
                v[j] = tempVet[j-1] + tempVet[j]
            v[i+1] = 1
            print(tempVet[c], sep=' ', end=" ", flush=True)
            #c=0
            print()

def generaTriangoloMeglio(stop):
    #Ma questo non fa l'ultima riga
    v = [0]*(stop+1)
    v[0] = 1
    v[1] = 1
    for i in range(1,stop):
        tempVet = v[:]
        c=0
        for j in range(1,i):
            print(tempVet[c], sep=' ', end=" ", flush=True)
            c=c+1
            v[j] = tempVet[j-1] + tempVet[j]
        v[i] = 1
        print(tempVet[c], sep=' ', end=" ", flush=True)
        print()

#ass=[0]*(15+1)
#print (ricTring(15,ass))
num = input("Dammi il numero")
generaTriangoloMeglio(int(num))
#generaTriangolo(int(num))
#print(triangle(int(num)))
