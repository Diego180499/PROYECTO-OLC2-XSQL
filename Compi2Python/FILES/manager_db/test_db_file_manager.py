from db_file_manager import *


eliminar_columna('escuela','usuario','campo_prueba')





def crear_objeto_base_de_datos():
    campos: Campo = []
    campo: Campo = Campo('id_ciente', 'varchar', '0', '1', '', '')
    campo2: Campo = Campo('nombre_cliente', 'varchar', '0', '0', '', '')
    campos.append(campo)
    campos.append(campo2)

    tablas: Tabla = []
    tabla: Tabla = Tabla('cliente', campos)
    tablas.append(tabla)

    base_de_datos: BaseDatos = BaseDatos('banco', tablas)
    return base_de_datos

