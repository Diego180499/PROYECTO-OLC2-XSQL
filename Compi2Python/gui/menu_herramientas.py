import os
from tkinter import *
from tkinter.filedialog import askopenfilename, asksaveasfilename

from gui.conector import Conector
from gui.menu_archivo import MenuArchivo
from utils.archivo import Archivo
from gui.frame_arbol import FrameArbol
from gui.frame_pestanas import FramePestanas
from gui.frame_salida import FrameSalida
from tkinter import messagebox as MessageBox


class MenuHerramientas(Menu):

    def __init__(self, ventana_principal, frame_arbol):
        super().__init__(ventana_principal.ventana)
        self.ventana_principal = ventana_principal
        self.frame_pestanas=ventana_principal.frame_pestanas
        self.frame_salida=ventana_principal.frame_salida
        self.frame_arbol = frame_arbol

        self.add_command(label='Base de Datos', command=self.evento_menu_bbdd)
        self.add_cascade(label='SQL', menu=self.agregar_menu_sql())
        self.add_command(label='Exportar', command=self.evento_menu_exportar)
        self.add_command(label='Importar', command=self.evento_menu_importar)
        self.add_command(label='Actualizar Bases de Datos', command=self.actualizar_arbol_bd)


    # ----------------------------------------------------------MENU----------------------------------------------------------
    # Eventos Menu
    def evento_menu_nuevo(self):
        self.frame_pestanas.agregar_pestana(Archivo())

    def evento_menu_bbdd(self):
        print("menu 'Base de Datos' pulsado")

    def evento_menu_ejecutar_query(self):
        conector=Conector()
        _,contenido=self.frame_pestanas.obtener_ubicacion_contenido_desde_pestana_activa()

        #el resultado DEBE ser una matriz
        resultado=conector.compilar(contenido)

        ### acciones de prueba  ####
        ### acciones de la tabla
        self.frame_salida.limpiar_tabla()
        self.frame_salida.construir_tabla(resultado)

    def evento_menu_exportar(self):
        print("menu 'exportar' pulsado")

    def evento_menu_importar(self):
        print("menu 'importar' pulsado")


    def agregar_menu_sql(self):
        menu_sql = Menu(self)
        menu_sql.add_command(label='Nueva Query', command=self.evento_menu_nuevo)
        menu_sql.add_command(label='Ejecutar Query', command=self.evento_menu_ejecutar_query)
        return menu_sql

    def actualizar_arbol_bd(self):
        conector = Conector()
        self.frame_arbol.limpiar_arbol()
        self.ventana_principal._listar_nombres_bd(conector)