from src.FILES.manager_db.db_file_manager import *

### Esta clase es la que tendra comunicación con la gramatica
class DataBaseRepository:

    def __init__(self):
        pass

    def crear_bd(self, nombre_bd):
        base_datos: BaseDatos = BaseDatos(nombre_bd,[])
        if self.existe_bd(nombre_bd) :
            matriz_respuesta = ["Mensaje de Error",f'La base de datos con el nombre "{base_datos.nombre}" ya existe en el sistema']
            return matriz_respuesta
        crear_base_de_datos_a_xml(base_datos.nombre, base_datos)
        matriz_respuesta = ["Mensaje", "Se ha creado la base de datos correctamente"]
        return matriz_respuesta


    def eliminar_bd(self, nombre_bd):

        if self.existe_bd(nombre_bd) :
            eliminar_base_de_datos(nombre_bd)
            return ["Mensaje",f'Se ha eliminado la base de datos "{nombre_bd}" ']
        return ["Mensaje de Error",f'No se ha encontrado la base de datos "{nombre_bd}" ']


    def guardar_procedimiento(self,nombre_bd, nombre_procedimiento):
        procedimiento : Procedimiento = procedimieto(nombre_procedimiento)
        crear_procedimiento(nombre_bd,procedimiento)


    def existe_bd(self, nombre_bd):
        nombres_bd : [] = obtener_nombres_de_bases_de_datos()

        for nombre in nombres_bd :
            if nombre == f'{nombre_bd}.xml' :
                return True
        return False