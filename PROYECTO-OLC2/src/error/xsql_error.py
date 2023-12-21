class xsql_error:

    def __init__(self, descripcion, valor, tipo, linea):
        self.descripcion = descripcion
        self.valor = valor
        self.tipo = tipo
        self.linea = linea

    def to_string(self):
        return f'descripcion: {self.descripcion} valor:{self.valor} tipo:{self.tipo} linea:{self.linea}'