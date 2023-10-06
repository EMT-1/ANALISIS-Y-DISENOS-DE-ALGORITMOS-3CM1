def merge_sort(mein):
    if len(mein) <=1:
        return mein
    #Dividir. obtener la mitad del arrreglo
    mitad=len(mein)//2
    izq=mein[:mitad]
    der=mein[mitad:]

    #Conquistar
    #llamamos de manera recursiva 
    izq=merge_sort(izq)
    der=merge_sort(der)

    #Combinar
    return merge(izq, der)

def merge (izq, der):
    gott =[]
    i_izq, i_der = 0, 0
    while(i_izq < len(izq) and i_der < len(der)):
        if (izq[i_izq]<der[i_der]):
            gott.append(izq[i_izq])
            i_izq+=1

        else:
            gott.append(der[i_der])
            i_der+=1

    #Agregar los valores restantes
    gott.extend(izq[i_izq:])
    gott.extend(der[i_der:])
    return gott
if __name__=="__main__":
    arreglo =[5, 2, 6, 3, 9, 6, 10]
    print("Arreglo no ordenado", arreglo)
    gott=merge_sort(arreglo)
    print ("Arreglo ordenado", gott)

    #El codigo tiene una complegidad de o(n log n)