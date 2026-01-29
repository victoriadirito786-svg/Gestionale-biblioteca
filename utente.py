class Utente:
    def __init__(self, nome_utente, numero_tessera, libri_in_prestito, storico):        
        self.nome_utente = nome_utente
        self.numero_tessera = numero_tessera
        self.libri_in_prestito = []
        self.storico = []
        
        def __repr__(self):
            return f"Utente({self.nome_utente},Numero{self.numero_tessera},Libri{self.libri_in_prestito},Storico{self.storico})"