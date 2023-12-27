class ManejadorDB:

    def __init__(self):
        """Initializes the data."""
        self.basesDatos = []

    def addBaseDatos(self, baseDatos):
        self.basesDatos.append(baseDatos)

    def diccionarioCampos(self, campos):
        retCamp = []
        for campo in campos:
            retCamp.append(campo.nombre)
        return retCamp

    def diccionarioTablas(self, tablas):
        retTab = []
        for tabla in tablas:
            temTab = {
                tabla.nombre: {
                    "campos": self.diccionarioCampos(tabla.campos)
                }
            }
            retTab.append(temTab)

        return retTab

    def getDiccionario(self):
        baseD = self.basesDatos[0]
        return {
            baseD.nombre: {
                "tablas": self.diccionarioTablas(baseD.tablas)
            }
        }
