class Autore:
    def __init__(self, nome_autore, nazionalita_autore):
        self.nome_autore = nome_autore
        self.nazionalita_autore = nazionalita_autore

        def __repr__(self):
            return f"Autore({self.nome_autore},Nazionalita{self.nazionalita_autore})"
        
