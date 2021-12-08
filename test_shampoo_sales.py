#==============================
#  Librerie da importare
#==============================

import unittest
from shampoo_sales import CSVFile

#==============================
#  Classe padre per Testing
#==============================

class Test(unittest.TestCase):

    #Usare 'python -m unittest test_shampoo_sales.py' per eseguire il test di tutti i metodi

    def test_getName(self):
        name = r"C:\Users\Davide\Documents\Università\ProgrammazioneLab\Esercizi\Shampoo_sales.csv"
        c = CSVFile(name)
        test_result = [['01-01-2012', '266.0'], ['01-02-2012', '145.9'], ['01-03-2012', '183.1'], ['01-04-2012', '119.3'], ['01-05-2012', '180.3'], ['01-06-2012', '168.5'], ['01-07-2012', '231.8'], ['01-08-2012', '224.5'], ['01-09-2012', '192.8'], ['01-10-2012', '122.9'], ['01-11-2012', '336.5'], ['01-12-2012', '185.9'], ['01-01-2013', '194.3'], ['01-02-2013', '149.5'], ['01-03-2013', '210.1'], ['01-04-2013', '273.3'], ['01-05-2013', '191.4'], ['01-06-2013', '287.0'], ['01-07-2013', '226.0'], ['01-08-2013', '303.6'], ['01-09-2013', '289.9'], ['01-10-2013', '421.6'], ['01-11-2013', '264.5'], ['01-12-2013', '342.3'], ['01-01-2014', '339.7'], ['01-02-2014', '440.4'], ['01-03-2014', '315.9'], ['01-04-2014', '439.3'], ['01-05-2014', '401.3'], ['01-06-2014', '437.4'], ['01-07-2014', '575.5'], ['01-08-2014', '407.6'], ['01-09-2014', '682.0'], ['01-10-2014', '475.3'], ['01-11-2014', '581.3'], ['01-12-2014', '646.9']]
        self.assertEqual(c.__getData__(),test_result)

    def test_getData(self):
        name = r"C:\Users\Davide\Documents\Università\ProgrammazioneLab\Esercizi\Shampoo_sales.csv"
        c = CSVFile(name)
        self.assertEqual(c.name, name)
 
    def test_getDataOneLine(self):
        name = r"C:\Users\Davide\Documents\Università\ProgrammazioneLab\Esercizi\Shampoo_sales.csv"
        c = CSVFile(name)
        test_result = [['01-10-2012', '122.9\n'], ['01-11-2012', '336.5\n'], ['01-12-2012', '185.9\n'], ['01-01-2013', '194.3\n'], ['01-02-2013', '149.5\n'], ['01-03-2013', '210.1\n'], ['01-04-2013', '273.3\n'], ['01-05-2013', '191.4\n'], ['01-06-2013', '287.0\n'], ['01-07-2013', '226.0\n'], ['01-08-2013', '303.6\n']]
        self.assertEqual(c.__getDataOneline__(10,20),test_result)

    def test_sumShampoo(self):
        name = r"C:\Users\Davide\Documents\Università\ProgrammazioneLab\Esercizi\Shampoo_sales.csv"
        c = CSVFile(name)
        self.assertEqual(c.__sumShampooPrice__(),11253.599999999999)
    
