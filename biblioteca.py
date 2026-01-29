class Biblioteca:
    def __init__(self,catalogo_libri, utenti):
        self.catalogo_libri = catalogo_libri
        self.utenti = utenti

    def aggiungi_libro(self, titolo,isbn, nome_autore, nazionalita_autore):
        self.titolo = titolo
        self.isbn = isbn
        self.nome_autore = nome_autore
        self.nazionalita_autore = nazionalita_autore