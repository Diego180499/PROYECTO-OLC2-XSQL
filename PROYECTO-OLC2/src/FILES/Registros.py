class Registros:
    def __init__(self, baseDatos, tabla, registros):
        """Initializes the data."""
        self.baseDatos = baseDatos
        self.tabla = tabla
        self.registros = registros

    def matriz(self):
        matriz = []
        valores_campos = []
        for campo in self.registros[0].campos :
            valores_campos.append(campo)
        matriz.append(valores_campos)
        for registro in self.registros:
            filaAdd = []
            for textVal in registro.valores:
                filaAdd.append(textVal)
            matriz.append(filaAdd)
        return matriz
