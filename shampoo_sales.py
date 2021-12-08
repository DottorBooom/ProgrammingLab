#==============================
#  Librerie da importare
#==============================

import itertools

class ErroreNome():
    pass

#==============================
#  Classe per file CSV
#==============================

class CSVFile:

    #Primo metedo eseguito quando viene creata un instanza della classe CSVFile
    def __init__(self, name):
    
        #Setto il nome del file all' attributo passato come attributo alla classe CSVFile
        self.name = name  
        
        #Provo ad aprirlo e leggere una riga per testare il nome del file. Utilizzo una variabile 'can_read' per tenere traccia di questa verifica
        self.can_read = True
        try:
            my_file = open(self.name, 'r')
            my_file.readline()
            my_file.close()
        except Exception as e:
            self.can_read = False
            print('Errore in apertura del file: "{}"'.format(e))

    #Metodo per la somma di tutti i prezzi di 'shampoo_sales' senza l'utilizzo della funzione built-in 'sum'
    def __sumShampooPrice__(self): 
        if not self.can_read:
            
            # Se nell'init ho settato can_read a False vuol dire che
            # il file non poteva essere aperto o era illeggibile
            print('Errore, file non aperto o illeggibile')
            
            # Esco dalla funzione tornando "niente".
            return None

        else:
            som = 0
            my_file = open(self.name, 'r')
            for i in my_file:
                som += float((i.split(",")[1]))
            my_file.close()
            return som

    #Metodo one-line che utilizza la funzione built-in sum
    def __sumOneLine__(self):
        if not self.can_read:
            
            # Se nell'init ho settato can_read a False vuol dire che
            # il file non poteva essere aperto o era illeggibile
            print('Errore, file non aperto o illeggibile')
            
            # Esco dalla funzione tornando "niente".
            return None

        else:
            my_file = open(self.name, 'r')
            j = sum((float(i.split(",")[1]) for i in my_file))
            my_file.close()
            return j

    #Metodo che converte, e ritorna, il file in una lista di liste
    def __getData__(self):
        
        if not self.can_read:
            
            # Se nell'init ho settato can_read a False vuol dire che
            # il file non poteva essere aperto o era illeggibile
            print('Errore, file non aperto o illeggibile')
            
            # Esco dalla funzione tornando "niente".
            return None

        else:
            # Inizializzo una lista vuota per salvare tutti i dati
            data = []
    
            # Apro il file
            my_file = open(self.name, 'r')

            # Leggo il file linea per linea
            for line in my_file:
                
                # Faccio lo split di ogni linea sulla virgola
                elements = line.split(',')
                
                # Posso anche pulire il carattere di newline 
                # dall'ultimo elemento con la funzione strip():
                elements[-1] = elements[-1].strip()
                
                # p.s. in realta' strip() toglie anche gli spazi
                # bianchi all'inizio e alla fine di una stringa.
    
                # Se NON sto processando l'intestazione...
                if elements[0] != 'Date':
                        
                    # Aggiungo alla lista gli elementi di questa linea
                    data.append(elements)
            
            # Chiudo il file
            my_file.close()
            
            # Quando ho processato tutte le righe, ritorno i dati
            return data

    #Metodo che converte, e ritorna, il file in una lista di liste (fatto da me)
    def __getDataOneline__(self,start,end):
        if not self.can_read:
            
            # Se nell'init ho settato can_read a False vuol dire che
            # il file non poteva essere aperto o era illeggibile
            print('Errore, file non aperto o illeggibile')
            
            # Esco dalla funzione tornando "niente".
            return None

        else:
            my_file = open(self.name, 'r')
            if((start and end) == None):
                j = [(i.split(",")) for i in self.file]
            elif end == -1:
                j = [(i.split(",")) for i in itertools.islice(my_file,start-1,None,1)]
            else:
                j = [(i.split(",")) for i in itertools.islice(my_file,start-1,end,1)]
            my_file.close()
            return j

#==============================
# Classe per file NumericalCSV
#==============================

class NumericalCSVFile(CSVFile):

    #Reimportare il metodo della classe madre
    def __init__(self, name):
        super().__init__(name)
    
    #Metodo che converte n colonne del file, esclusa la prima, in interi (fatto da me)
    def __strToFloat__(self):
        j = []
        my_file = open(self.name, 'r')
        for i in my_file:
            try:
                j.append([i.split(",")[0],float(i.split(",")[1])])
            except ValueError:
                print('\nNon posso convertire "i[0]" a valore numerico!')
                print('Ho avuto un errore di VALORE. "i[0]" valeva: {}'.format(i.split(",")[1]))
            except TypeError:
                print('\nNon posso convertire "i[0]" a valore numerico!')
                print('Ho avuto un errore di TIPO. "i[0]" era di tipo: {}'.format(type(i.split(",")[1])))
        my_file.close()
        return j
    
    #Metodo che converte n colonne del file, esclusa la prima, in interi (del prof)
    def __getData__(self):
        
        # Chiamo la __getData__ del genitore 
        string_data = super().__getData__()
        
        # Preparo lista per contenere i dati ma in formato numerico
        numerical_data = []
        
        # Ciclo su tutte le "righe" corrispondenti al file originale 
        for string_row in string_data:
            
            # Preparo una lista di supporto per salvare la riga
            # in "formato" nuumerico (tranne il primo elemento)
            numerical_row = []
            
            # Ciclo su tutti gli elementi della riga con un
            # enumeratore: cosi' ho gratis l'indice "i" della
            # posizione dell'elemento nella riga.
            for i,element in enumerate(string_row):
                
                if i == 0:
                    # Il primo elemento della riga lo lascio in formato stringa
                    numerical_row.append(element)
                    
                else:
                    # Converto a float tutto gli altri. Ma se fallisco, stampo
                    # l'errore e rompo il ciclo (e poi saltero' la riga).
                    try:
                        numerical_row.append(float(element))
                    except Exception as e:
                        print('Errore in conversione del valore "{}" a numerico: "{}"'.format(element, e))
                        break
                
            # Alla fine aggiungo la riga in formato numerico alla lista
            # "esterna", ma solo se sono riuscito a processare tutti gli
            # elementi. Qui controllo per la lunghezza, ma avrei anche potuto
            # usare una variabile di supporto o fare due break in cascata.
            if len(numerical_row) == len(string_row):
                numerical_data.append(numerical_row)

        return numerical_data

#Metodo che verifica la veridicità dei dati inseriti
def sanifica(x,bool):
    try:    
        return int(x)
    except TypeError:
        print('\nNon posso convertire "i[0]" a valore numerico!')
        print('Ho avuto un errore di TIPO. "i[0]" era di tipo: {}'.format(type(x)))
        if bool: return 1
        else: return -1
    except ValueError:
        print('\nNon posso convertire "i[0]" a valore numerico!')
        print('Ho avuto un errore di VALORE. "i[0]" valeva: {}'.format(x))
        if bool: return 1
        else: return -1

#==============================
#  Corpo del programma
#==============================

def main():

    #Editare l'hashtag per shiftare tra i file e testare gli errori
    name = r"C:\Users\Davide\Documents\Università\ProgrammazioneLab\Esercizi\Shampoo_sales.csv"
    #name = r"C:\Users\Davide\Documents\Università\ProgrammazioneLab\Esercizi\Shampoo_sales_errors.csv"

    #Alzare un errore se il percorso del file non è una stringa
    if type(name) is not str:
        raise ErroreNome("Il nome de file passato non è una stringa")   
    
    #Instanziare un oggetto della classe CSVFile passando come parametro il percorso del file
    mio_file = CSVFile(name)
    print('Nome del file: "{}"'.format(mio_file.name))
    print('Somma dei prezzi dello shampoo: "{}"'.format(mio_file.__sumOneLine__()))
    print('Dati contenuti nel file: "{}"'.format(mio_file.__getData__()))

    #Instanziare un oggetto della classe NumericalCSVFile passando come parametro il percorso del file
    mio_file_numerico = NumericalCSVFile(name)
    print('Nome del file: "{}"'.format(mio_file_numerico.name))
    print('Dati contenuti nel file: "{}"'.format(mio_file_numerico.__getData__()))

    #Prendere valori in input e sanificarli
    start = input("Inserire la riga di partenza: ")
    end = input("Inserire la riga di terminazione: ")
    start = sanifica(start,True)
    end = sanifica(end,False)
    
    #Dopo aver sanificato i dati, eseguire il "getData" passando i valori come parametro
    print('\n' + str(mio_file.__getDataOneline__(start,end)))   

if __name__ == "__main__":
    main()