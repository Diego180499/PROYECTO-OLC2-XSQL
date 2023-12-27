class Campo:
    def __init__(self, nombre, tipoDato, nulo, llavePrim=None, tablaRef=None, campoRef=None):
        """Initializes the data."""
        self.nombre = nombre
        self.tipoDato = tipoDato
        if llavePrim != None:
            self.llavePrim = llavePrim
        self.nulo = nulo
        if tablaRef != None and campoRef != None:
            self.tablaRef = tablaRef
            self.campoRef = campoRef

