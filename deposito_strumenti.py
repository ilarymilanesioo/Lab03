import csv

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
        strumenti={}
        try:
            with open(file_path,'r',encoding='utf-8') as file:
                reader=csv.DictReader(file)
                for riga in reader:
                    if not riga:
                        continue
                    codice=riga['codice']
                    tipo=riga['tipo']
                    marca=riga['marca']
                    anno=int(riga['anno'])
                    valore=float(riga['prezzo'])
                    self.strumenti[codice]={
                        'tipo':tipo,
                        'marca':marca,
                        'anno':anno,
                        'valore':valore
                    }
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
        # TODO

    def nuovo_prestito(self, data, id_strumento, cognome_allievo):
        """Crea un nuovo prestito"""
        # TODO

    def termina_prestito(self, id_prestito):
        """Termina un prestito in atto"""
        # TODO
