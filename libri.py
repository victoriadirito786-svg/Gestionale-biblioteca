class Libro:
    def __init__(self, titolo, codice_isbn, libro_disponibile, data_prestito):
        self.titolo = titolo
        self.codice_isbn = codice_isbn
        self.libro_disponibile = True
        self.data_prestito = None
