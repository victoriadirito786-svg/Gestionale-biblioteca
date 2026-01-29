class Libro:
    def __init__(self, titolo, codice_isbn, libro_disponibile, data_prestito, data_restituzione):
        self.titolo = titolo
        self.codice_isbn = codice_isbn
        self.libro_disponibile = True
        self.data_prestito = None
        self.data_restituzione = None

    def __str__(self):
        return f"Titolo: {self.titolo}, isbn: {self.codice_isbn}, disponibile: {self.libro_disponibile}, prestito: {self.data_prestito}, restituzione: {self.data_retribuzione}"
    
    def titolo(self):
        return self.titolo
    
    def codice_isbn(self):
        return self.codice_isbn
    
    def libro_disponibile(self):
        return self.libro_disponibile
    
    def data_prestito(self):
        return self.data_prestito
    
    def data_restituzione(self):
        return self.data_restituzione
    
    