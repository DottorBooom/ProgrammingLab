#Dato il file shampoo_sales.txt o .csv, sommare tutti i valori degli shampi e stamparli a video.

import sys

#Versione semplice senza l'utilizzo della funzione sum
def somma_v1(my_file): 
    som = 0
    for i in my_file:
        som += float((i.split(",")[1]))
    return som

#Versione one-line code con utilizzo della funzione sum
def somma_v2(my_file):
    return sum((float(i.split(",")[1]) for i in my_file))

def main(): 
    with open(r'C:\Users\Davide\Documents\Università\ProgrammazioneLab\Esercizi\Shampoo_sales.txt', 'r') as f:
        print(somma_v1(f)) #Cambiare 1 o 2 dopo v per testare le due funzioni
        f.close()

if __name__ == '__main__':
    sys.exit(main())