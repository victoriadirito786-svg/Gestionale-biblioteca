class Libro:
    def __init__(self, titolo, codice_isbn, libro_disponibile, data_prestito, data_restituzione):
        self.titolo = titolo
        self.codice_isbn = codice_isbn
        self.libro_disponibile = libro_disponibile
        self.data_prestito = data_prestito
        self.data_restituzione = data_restituzione

    def __repr__(self):
        return f"Titolo: {self.titolo}, isbn: {self.codice_isbn}, disponibile: {self.libro_disponibile}, prestito: {self.data_prestito}, restituzione: {self.data_retribuzione}"
    
    