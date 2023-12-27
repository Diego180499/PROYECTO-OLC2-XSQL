from tkinter import *
from tkinter import simpledialog, messagebox
from tkinter.filedialog import asksaveasfilename
from gui.conector import Conector
from src.FILES.manager_db import db_file_manager, db_to_xml
from src.utils.archivo import Archivo


class MenuHerramientas(Menu):

    def __init__(self, ventana_principal):
        super().__init__(ventana_principal.menu)
        self.ventana_principal = ventana_principal
        self.frame_pestanas = ventana_principal.frame_pestanas
        self.frame_salida = ventana_principal.frame_salida
        self.frame_arbol = ventana_principal.frame_arbol
        self.iconos = ventana_principal.iconos
        self.add_cascade(label='Base de Datos', image=self.iconos['base-de-datos'], compound="left",
                         menu=self.agregar_menu_bbdd())
        self.add_cascade(label='SQL', image=self.iconos['sql'], compound="left", menu=self.agregar_menu_sql())

    # ----------------------------------------------------------MENU----------------------------------------------------------
    # Eventos Menu
    def evento_menu_nuevo(self):
        self.frame_pestanas.agregar_pestana(Archivo())

    def evento_menu_ejecutar_query(self):
        conector = Conector()
        _, contenido = self.frame_pestanas.obtener_ubicacion_contenido_desde_pestana_activa()
        if contenido is None or contenido == '':
            return

        # el resultado DEBE ser una matriz
        resultados_finales = conector.compilar(contenido)

        ### acciones de prueba  ####
        ### acciones de la tabla
        self.frame_salida.tabla_salida.limpiar_tabla()
        if len(resultados_finales[0]) > 0:
            self.frame_salida.tabla_salida.construir_tabla(resultados_finales[0])

        self.frame_salida.tabla_simbolos.limpiar_tabla()
        if len(resultados_finales[1]) > 0:
            self.frame_salida.tabla_simbolos.construir_tabla(resultados_finales[1])

        self.frame_salida.tabla_errores.limpiar_tabla()
        if len(resultados_finales[2]) > 0:
            self.frame_salida.tabla_errores.construir_tabla(resultados_finales[2])

        self.frame_salida.limpiar_text_c3d()
        if len(resultados_finales[3]) > 0:
            self.frame_salida.agregar_text_c3d("hola rey")

    def evento_crear_dump(self):
        nombre_bbdd = simpledialog.askstring("Crear Dump", "Escriba el nombre de la base de datos para crear dump file",
                                             parent=self.ventana_principal.ventana)
        if nombre_bbdd is None:
            return
        print("Base de datos seleccionada: ", nombre_bbdd)

        bbdd = db_file_manager.obtener_base_de_datos(nombre_bbdd)
        if bbdd is None:
            messagebox.showerror("Crear Dump", "La base de datos ingresada no existe")
            return

        contenido_xml = db_to_xml.data_base_to_xml(bbdd)
        self.mostrar_ventana_guardar_archivo(contenido_xml)

    def evento_crear_bbdd(self):
        pass

    def evento_borrar_bbdd(self):
        pass

    def evento_actualizar_arbol_bbdd(self):
        conector = Conector()
        self.frame_arbol.limpiar_arbol()
        self.ventana_principal.__listar_nombres_bd__(conector)

    def agregar_menu_sql(self):
        menu_sql = Menu(self)
        menu_sql.add_command(label='Nueva Query', image=self.iconos['nueva-query'], compound="left",
                             command=self.evento_menu_nuevo)
        menu_sql.add_command(label='Ejecutar Query', image=self.iconos['ejecutar-query'], compound="left",
                             command=self.evento_menu_ejecutar_query)
        return menu_sql

    def agregar_menu_bbdd(self):
        menu_bbdd = Menu(self)
        menu_bbdd.add_command(label='Crear Base de Datos', image=self.iconos['crear_base_de_datos'], compound="left",
                              command=self.evento_crear_bbdd)
        menu_bbdd.add_command(label='Eliminar Base de Datos', image=self.iconos['borrar-base-de-datos'],
                              compound="left", command=self.evento_borrar_bbdd)
        menu_bbdd.add_command(label='Crear Dump', image=self.iconos['crear-dump'], compound="left",
                              command=self.evento_crear_dump)
        menu_bbdd.add_command(label='Actualizar Bases de Datos', image=self.iconos['actualizar'], compound="left",
                              command=self.evento_actualizar_arbol_bbdd)
        return menu_bbdd

    def mostrar_ventana_guardar_archivo(self, contenido):
        ubicacion = asksaveasfilename(filetypes=[('Archivos Dump', '*.xml')])
        if ubicacion == '':
            return None
        with open(ubicacion, 'w') as archivo:
            archivo.write(contenido)
