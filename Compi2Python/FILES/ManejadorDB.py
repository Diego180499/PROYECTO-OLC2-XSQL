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
               "tabla": {
               "nombre": tabla.nombre,
               "campos": self.diccionarioCampos(tabla.campos)
                }
           }
           retTab.append(temTab)

       return retTab

    def diccionarioBasesDatos(self):
       retDB = []
       for baseD in self.basesDatos:
           temDB = {
               "base_de_datos":{
                   "nombre": baseD.nombre,
                   "tablas": self.diccionarioTablas(baseD.tablas)
               }
           }
           retDB.append(temDB)
       return retDB

    def getDiccionario(self):

        diccionario = {
            "DBMS": {
                "bases_de_datos":self.diccionarioBasesDatos()
            }
        }
        valor = diccionario
        return diccionario
