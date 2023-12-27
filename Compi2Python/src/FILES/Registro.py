class Registro:
    def __init__(self, campos : [], valores : []):
        """Initializes the data."""
        self.campos = campos
        self.valores = valores

    def __str__(self):
        return f"{self.valores}"
