import csv
from operator import attrgetter

class Strumento:
    def __init__(self, codice, tipo, marca, anno_acquisto, valore):
        self.codice = codice
        self.tipo = tipo
        self.marca = marca
        self.anno_acquisto = anno_acquisto
        self.valore = valore

    def __str__(self):
        return f"{self.codice} - {self.tipo} {self.marca} ({self.anno_acquisto}), €{self.valore}"

class Prestito:
    def __init__(self, codice, data, id_strumento, cognome_allievo):
        self.codice = codice
        self.data = data
        self.id_strumento = id_strumento
        self.cognome_allievo = cognome_allievo

    def __str__(self):
        return f"Prestito {self.codice}: Strumento {self.id_strumento} affidato a {self.cognome_allievo} in data {self.data}"

class DepositoStrumenti:
    def __init__(self, nome, responsabile):
        #per creare un oggetto DepositoStrumenti, chi usa il codice deve per forza fornirmi un nome e un responsabile
        """Inizializza gli attributi e le strutture dati"""
        self.nome=nome
        self.responsabile=responsabile
        #strumenti non serve metterlo tra le parentesi dell'init perché:
        #un deposito appena creato parte quasi sempre vuoto (self.strumenti = {}).
        #i dati degli strumenti non li conosco al momento della creazione, ma li caricherò solo dopo chiamando la funzione carica_file_strumenti(file_path).
        self.strumenti={}
        # TODO

    def carica_file_strumenti(self, file_path):
        """Carica gli strumenti dal file"""
        try:
            with open(file_path,'r',encoding='utf-8') as file:
                reader=csv.reader(file)
                for riga in reader:
                    if not riga:
                        continue
                    codice= riga[0].strip()
                    tipo= riga[1].strip()
                    marca= riga[2].strip()
                    anno= int(riga[3].strip())
                    valore= float(riga[4].strip())
                    #non creo dizionario perchè con attrgetter non funziona poi
                    strumento=Strumento(codice,tipo,marca,anno,valore) #creo classe strumento
                    self.strumenti[codice]=strumento
        except FileNotFoundError:
            print('errore')
        # TODO

    def aggiungi_strumento(self, codice ,tipo, marca, anno_acquisto, valore):
        """Aggiunge uno strumento nel deposito: aggiunge solo nel sistema e non aggiorna il file"""
        for lista_strumenti in self.strumenti.values():
            if lista_strumenti['tipo'] == tipo and lista_strumenti['marca'] == marca and lista_strumenti['anno'] == anno_acquisto and lista_strumenti['valore'] == valore:
                print("Errore: Uno strumento identico è già presente nel deposito.")
                return
        if codice in self.strumenti:
            print(f"Errore: Il codice '{codice}' è già esistente.")
            return
        self.strumenti[codice]={
            'tipo': tipo,
            'marca': marca,
            'anno': anno,
            'valore': valore
            }
        # TODO
    def strumenti_ordinati_per_marca(self):
        """Ordina gli strumenti per marca in ordine alfabetico"""
        return sorted(self.strumenti, key=attrgetter('marca'), reverse=True)
        # TODO

    def nuovo_prestito(self, data, id_strumento, cognome_allievo):
        """Crea un nuovo prestito"""
        if id_strumento not in self.strumenti:
            raise Exception('errore')
        for prestito in self.prestiti.values():
            if prestito.id_strumento==id_strumento:
                raise Exception("Lo strumento è già in prestito.")

        id_prestito = f"P{len(self.prestiti) + 1}"

        prestito = Prestito(id_prestito, data, id_strumento, cognome_allievo)

        self.prestiti[id_prestito] = prestito

        return prestito
        # TODO

    def termina_prestito(self, id_prestito):
        """Termina un prestito in atto"""

        def termina_prestito(self, id_prestito):
            """Termina un prestito in atto"""
            if id_prestito not in self.prestiti:
                raise Exception("Il codice del prestito inserito non esiste.")

            del self.prestiti[id_prestito]
        # TODO
