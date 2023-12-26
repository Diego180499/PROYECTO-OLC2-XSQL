import errno
import os
import pathlib
from tkinter import *


from gui.conector import Conector
from gui.frame_arbol import FrameArbol
from gui.frame_pestanas import FramePestanas
from gui.frame_salida import FrameSalida
from gui.menu_archivo import MenuArchivo
from gui.menu_herramientas import MenuHerramientas


class VentanaPrincipal:

    def __init__(self):
        # creacion de la ventana principal
        self.ventana = Tk()
        self.ventana.geometry("1200x640")
        self.ventana.resizable(False, False)
        self.ventana.iconbitmap('')
        self.ventana.title("Proyecto Compiladores 2")
        # añadimos los 3 frames principales
        self.frame_arbol = FrameArbol(self.ventana, width=350, height=600, row=0, column=0, rowspan=2)
        self.frame_pestanas = FramePestanas(self.ventana, width=750, height=270, row=0, column=1)
        self.frame_salida = FrameSalida(self.ventana, width=750, height=270, row=1, column=1)

        self.iconos=dict()
        current_dir = pathlib.Path(__file__).parent.resolve()  # current directory
        self.iconos['abrir']= PhotoImage(file=os.path.join(current_dir, 'resources','abrir-carpeta.png'))
        self.iconos['guardar']= PhotoImage(file=os.path.join(current_dir, 'resources','guardar.png'))
        self.iconos['guardar-como']= PhotoImage(file=os.path.join(current_dir, 'resources','guardar-como.png'))
        self.iconos['cerrar']= PhotoImage(file=os.path.join(current_dir, 'resources','cerrar.png'))
        self.iconos['nuevo-archivo'] = PhotoImage(file=os.path.join(current_dir, 'resources', 'nuevo-archivo.png'))



        # añadimos la barra de menú
        self.menu = Menu(self.ventana)
        self.menu_archivo = MenuArchivo(self)
        self.menu_herramientas = MenuHerramientas(self)

        self.menu.add_cascade(label='Archivo', menu=self.menu_archivo)
        self.menu.add_cascade(label='Herramientas', menu=self.menu_herramientas)

        self.ventana.config(menu=self.menu)

        # añadirmos evento del cierre de ventana
        self.ventana.protocol("WM_DELETE_WINDOW", self.menu_archivo.evento_menu_salir)

    def ejecutar(self):
        conector = Conector()
        ### listar archivos de las bases de datos ###
        self._listar_nombres_bd(conector)
        self.ventana.mainloop()

    def _listar_nombres_bd(self, conector):
        url_proyecto = f'resources/BASES_DE_DATOS_XML'
        nombres_bd = os.listdir(url_proyecto)  # obtiene una lista con todos los archivos que contenga mi carpeta
        for nombre_bd in nombres_bd:
            diccionario = conector.cargar_arbol(f'{url_proyecto}/{nombre_bd}')
            self.frame_arbol.generar_arbol(diccionario=diccionario)
