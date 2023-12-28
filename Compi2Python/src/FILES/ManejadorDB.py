from src.FILES.Procedimiento import Procedimiento


class ManejadorDB:

    def __init__(self):
        """Initializes the data."""
        self.basesDatos = []

    def addBaseDatos(self, baseDatos):
        self.basesDatos.append(baseDatos)

    def generateDiccionario(self):

        for base in self.basesDatos:
            pass

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

    def diccionarioProcedimientos(self, procedimientos : Procedimiento = []):
        nombres_procedimientos = []
        for procedimiento in procedimientos :
            nombres_procedimientos.append(procedimiento.nombre)
        return nombres_procedimientos

    def getDiccionario(self):
        baseD = self.basesDatos[0]
        return {
            baseD.nombre: {
                "tablas": self.diccionarioTablas(baseD.tablas),
                "procedimientos": self.diccionarioProcedimientos(baseD.procedimientos)
            }
        }
