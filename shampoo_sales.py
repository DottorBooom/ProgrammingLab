#Dato il file shampoo_sales.txt o .csv, sommare tutti i valori degli shampi e stamparli a video.

from os import name
import sys

class CSVFile:

    def __init__(self, name):
        self.name = name

    #Versione semplice senza l'utilizzo della funzione sum
    def somma_v1(my_file): 
        som = 0
        for i in my_file:
            som += float((i.split(",")[1]))
        return som

    #Versione one-line code con utilizzo della funzione sum
    def somma_v2(my_file):
        return sum((float(i.split(",")[1]) for i in my_file))


    def get_data(my_file):
        j = []
        for i in my_file:
            j.append(i.split(","))
        return j
        
def main():
    name = r"C:\Users\Davide\Documents\Università\ProgrammazioneLab\Esercizi\Shampoo_sales.csv"
    with open(name, 'r') as f: #Ricordarsi di modificare il percorso del proprio file
        c = CSVFile(name)
        print(CSVFile.get_data(f))
        print(c.name)
    f.close()

main()