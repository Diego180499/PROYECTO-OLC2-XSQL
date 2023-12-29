from src.FILES.manager_db.db_file_manager import *
from src.FILES.manager_db.record_file_manager import *
from src.repository.table.table_repository import TableRepository


class RecordRepository:


    def __init__(self):
        self.tabla_repo : TableRepository = TableRepository()


    def insertar_registro(self, nombre_bd, nombre_tabla, campos : [] , valores : []):
        registro : Registro = Registro(campos,valores)

        if self.campos_existen_en_tabla(nombre_bd, nombre_tabla, campos):
            insertar_registro(nombre_bd,nombre_tabla,registro) ## este metodo es de record_file_manager
            return ["Mensaje",f'Se ha creado un nuevo registro para la tabla "{nombre_tabla}"']

        return ["Mensaje de error", f'Los campos no coinciden con los campos de la tabla "{nombre_tabla}"']


    def obtener_registros_de_tabla(self, nombre_bd, nombre_tabla):
        if self.tabla_repo.existe_tabla_en_bd(nombre_bd, nombre_tabla) :
            lista_registros = obtener_registros_tabla_2(nombre_bd, nombre_tabla)
            return lista_registros
        return ["Mensaje de Error",f'La tabla "{nombre_tabla}" no se encuentra dentro de la base de datos "{nombre_bd}"']

    def eliminar_registro(self, nombre_bd, nombre_tabla, registros_a_eliminar : []):

        if self.tabla_repo.existe_tabla_en_bd(nombre_bd, nombre_tabla) :
            eliminar_registro(nombre_bd,nombre_tabla,registros_a_eliminar)  ### este metodo es de record_file_manager
            return ["Mensaje",f'Se ha eliminado el registro en la tabla "{nombre_tabla}"']

        return ["Mensaje de Error",f'La tabla "{nombre_tabla}" no se encuentra dentro de la base de datos "{nombre_bd}"']

    def vaciar_registros_de_tabla(self, nombre_bd, nombre_tabla):
        if self.tabla_repo.existe_tabla_en_bd(nombre_bd, nombre_tabla):
            registros_bd: [] = obtener_registros_tabla_2(nombre_bd, nombre_tabla)
            eliminar_registro(nombre_bd, nombre_tabla, registros_bd)
            return ["Mensaje", f'Se han eliminado los registros de la tabla "{nombre_tabla}"']
        return ["Mensaje de Error",f'La tabla"{nombre_tabla}" no pertenece a la base de datos "{nombre_bd}"']


    def campos_existen_en_tabla(self, nombre_bd, nombre_tabla, campos : []):
        campos_tabla = obtener_nombres_campos_tabla(nombre_bd, nombre_tabla)
        for campo in campos:
            if not (campo in campos_tabla):
                return False

        return True

#### ACTUALIZAR REGISTRO
    def actualizar_registro(self, nombre_bd, nombre_tabla, campos_a_actualzar : [] , valores_a_actualizar : [], registros_a_actualizar : [Registro] = []):

        for registro in registros_a_actualizar :
            if self.validar_campos_en_registro(campos_a_actualzar,registro) :
                ## elimino el registro anterior para insertar el actualizado
                registros_a_eliminar = []
                registros_a_eliminar.append(registro)
                self.eliminar_registro(nombre_bd,nombre_tabla,registros_a_eliminar)
                ### actualizado el registro que quiero insertar de nuevo
                self.actualizar_valores_registro(campos_a_actualzar,valores_a_actualizar,registro)
                self.insertar_registro(nombre_bd,nombre_tabla,registro.campos, registro.valores) ## actualiza el registro
        print("Se actualizaron los registros")
        matriz_respuesta = ["Mensaje", "Se actualizaron los registros"]
        return matriz_respuesta


    def validar_campos_en_registro(self, campos : [], registro : Registro):
        for campo in campos :
            if not (campo in registro.campos) :
                return False

        return True

    def actualizar_valores_registro(self, campos : [], valores : [], registro : Registro):

        indice = 0
        while indice < len(registro.campos) :
            indice_campo_a_actualizar = 0
            while indice_campo_a_actualizar < len(campos) :
                if registro.campos[indice] == campos[indice_campo_a_actualizar] :
                    registro.valores[indice] = valores[indice_campo_a_actualizar]
                indice_campo_a_actualizar += 1
            indice += 1
        return True


    # realiza la validación si ya existen registros de esta tabla
    # ó si es el primer registro de esta tabla.
    def es_primer_registro(self,nombre_bd,nombre_tabla):
        if existe_archivo_registros(nombre_bd,nombre_tabla) :
           return False
        return True

