import os
from tkinter import *

from gui.conector import Conector

from src.utils.archivo import Archivo


class MenuHerramientas(Menu):

    def __init__(self, ventana_principal):
        super().__init__(ventana_principal.menu)
        self.ventana_principal = ventana_principal
        self.frame_pestanas = ventana_principal.frame_pestanas
        self.frame_salida = ventana_principal.frame_salida
        self.frame_arbol = ventana_principal.frame_arbol
        self.iconos = ventana_principal.iconos
        self.add_command(label='Base de Datos', command=self.evento_menu_bbdd)
        self.add_cascade(label='SQL', menu=self.agregar_menu_sql())
        self.add_command(label='Actualizar Bases de Datos', command=self.actualizar_arbol_bd)

    # ----------------------------------------------------------MENU----------------------------------------------------------
    # Eventos Menu
    def evento_menu_nuevo(self):
        self.frame_pestanas.agregar_pestana(Archivo())

    def evento_menu_bbdd(self):
        print("menu 'Base de Datos' pulsado")

    def evento_menu_ejecutar_query(self):
        conector = Conector()
        _, contenido = self.frame_pestanas.obtener_ubicacion_contenido_desde_pestana_activa()

        # el resultado DEBE ser una matriz
        resultado = conector.compilar(contenido)

        ### acciones de prueba  ####
        ### acciones de la tabla
        self.frame_salida.limpiar_tabla()
        self.frame_salida.construir_tabla(resultado)

    def agregar_menu_sql(self):
        menu_sql = Menu(self)
        menu_sql.add_command(label='Nueva Query', image=self.iconos['nuevo-archivo'],compound="left", command=self.evento_menu_nuevo)
        menu_sql.add_command(label='Ejecutar Query', command=self.evento_menu_ejecutar_query)
        return menu_sql

    def actualizar_arbol_bd(self):
        conector = Conector()
        self.frame_arbol.limpiar_arbol()
        self.ventana_principal._listar_nombres_bd(conector)
