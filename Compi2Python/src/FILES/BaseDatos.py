class BaseDatos:
    def __init__(self, nombre, tablas):
        """Initializes the data."""
        self.nombre = nombre
        self.tablas = tablas
        self.procedimientos = []

    def set_procedimientos(self, procedimientos):
        self.procedimientos = procedimientos
