#Dato il file shampoo_sales.txt o .csv, sommare tutti i valori degli shampi e stamparli a video.

from os import close, name
import sys

class CSVFile:

    def __init__(self, name):
        self.name = name
        try:
            self.file = open(name, 'r')
        except:
            print('Il file non è stato trovato')

    #Versione semplice senza l'utilizzo della funzione sum
    def __somma_v1__(self): 
        som = 0
        for i in self.file:
            som += float((i.split(",")[1]))
        return som

    #Versione one-line code con utilizzo della funzione sum
    def __somma_v2__(self):
        return sum((float(i.split(",")[1]) for i in self.file))

    def __get_data__(self):
        j = []
        for i in self.file:
            j.append(i.split(","))
        return j    

class NumericalCSVFile(CSVFile):

    def __init__(self, name):
        super().__init__(name)
    
    def __strToFloat__(self):
        j = []
        for i in self.file:
            try:
                j.append([i.split(",")[0],float(i.split(",")[1])])
            except ValueError:
                print('Non posso convertire "i[0]" a valore numerico!')
                print('Ho avuto un errore di VALORE. "i[0]" valeva "{}".'.format(i.split(",")[1]))
            except TypeError:
                print('Non posso convertire "i[0]" a valore numerico!')
                print('Ho avuto un errore di TIPO. "i[0]" era di tipo "{}".'.format(type(i.split(",")[1])))
        return j
        
def main():
    name1 = r"C:\Users\Davide\Documents\Università\ProgrammazioneLab\Esercizi\Shampoo_sales.csv"
    name2 = r"C:\Users\Davide\Documents\Università\ProgrammazioneLab\Esercizi\Shampoo_sales_errors.csv"
    #Ricordarsi di modificare il percorso del proprio file
    c = NumericalCSVFile(name2)
    print(c.__strToFloat__())

main()  