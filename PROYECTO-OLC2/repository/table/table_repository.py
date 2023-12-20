from FILES.Tabla import Tabla
from FILES.manager_db.db_file_manager import *
from repository.data_base.data_base_repository import DataBaseRepository
class TableRepository:

    def __init__(self):
        pass


    def crear_tabla(self, nombre_tabla, nombre_bd):

        if self.existe_tabla_en_bd(nombre_bd,nombre_tabla):
            return [["Mensaje error"],[f'la tabla "{nombre_tabla}" ya existe en la base de datos "{nombre_bd}" ']]

        tabla : Tabla = Tabla(nombre_tabla,[])
        crear_tabla(nombre_bd,tabla)
        return [["Mensaje"],[f'Se ha creado la tabla "{nombre_tabla}", en la base de datos "{nombre_bd}"']]

    def eliminar_tabla(self, nombre_tabla, nombre_bd):

        if self.existe_tabla_en_bd(nombre_bd,nombre_tabla):
            eliminar_tabla(nombre_bd,nombre_tabla)
            return [["Mensaje"],[f'se ha eliminado la tabla "{nombre_tabla}" de la base de datos "{nombre_bd}"']]
        return [["Mensaje de Error"],[f'La tabla "{nombre_tabla}" no existe en la base de datos "{nombre_bd}"']]


    def agregar_campos_tabla(self,nombre_bd, nombre_tabla, campo : Campo):

        if self.existe_tabla_en_bd(nombre_bd,nombre_tabla):
            nombres_campos_tabla = obtener_campos_tabla(nombre_bd,nombre_tabla)
            if self.existe_campo_en_tabla(campo.nombre, nombres_campos_tabla) :
                return [["Mensaje de Error"],[f'El campo "{campo.nombre}" ya existe en la tabla "{nombre_tabla}" de la bd "{nombre_bd}"']]

            agregar_campo_tabla(nombre_bd,nombre_tabla,campo)
            return [["Mensaje"],[f'Se ha añadido el campo "{campo.nombre}" a la tabla "{nombre_tabla}" de la bd "{nombre_bd}']]


        return [["Mensaje de Error"],[f'No se encontró la tabla "{nombre_tabla}" en la base de datos "{nombre_bd}"']]

######## validaciones ########


    def existe_campo_en_tabla(self, nombre_campo, nombres_campos_tabla : []):
        for nombre_campo_tabla in nombres_campos_tabla :
            if nombre_campo_tabla == nombre_campo :
                return True

        return False

    def existe_tabla_en_bd(self, nombre_bd, nombre_tabla):

        nombres_tablas : [] = obtener_tablas_de_bd(nombre_bd)

        for nombre in nombres_tablas :
            if nombre == nombre_tabla :
                return True

        return False



### pruebas    ###
