class Utente:
    def __init__(self, nome_utente, numero_tessera, libri_in_prestito, storico):        
        self.nome_utente = nome_utente
        self.numero_tessera = numero_tessera
        self.libri_in_prestito = []
        self.storico = []

        def __str__(self):
            return f"Utente: {self.nome_utente}, Tessera: {self.numero_tessera}, Libri_in_prestito: {self.libri_in_prestito}, Storico: {self.storico}"

        def nome_utente(self):
            return self.nome_utente
        
        def tessera(self):
            return self.tessera
        
        def libri_in_prestito(self):
            return self.libri_in_prestito
        
        def storico(self):
            return self.storico
        
        def __repr__(self):
            return f"Utente({self.nome_utente}, {self.numero_tessera}, {self.libri_in_prestito}, {self.storico})"