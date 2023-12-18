from tkinter import *
from tkinter import messagebox as MessageBox
from tkinter.filedialog import askopenfilename, asksaveasfilename

from utils.archivo import Archivo


class MenuArchivo(Menu):

    def __init__(self, ventana_principal):
        super().__init__(ventana_principal.ventana)
        self.add_command(label='Abrir', command=self.evento_menu_abrir)
        self.add_command(label='Guardar', command=self.evento_menu_guardar)
        self.add_command(label='Guardar Como', command=self.evento_menu_guardar_como)
        self.add_command(label='Cerrar', command=self.evento_menu_cerrar)
        self.add_command(label='Salir', command=self.evento_menu_salir)
        self.frame_pestanas=ventana_principal.frame_pestanas


    # eventos barra de menú
    def evento_menu_abrir(self):
        ubicacion = self.mostrar_ventana_abrir_archivo()
        if ubicacion is None:
            return
        self.frame_pestanas.agregar_pestana(Archivo(ubicacion))

    def evento_menu_guardar(self):
        if not self.frame_pestanas.hay_pestanas():
            return
        self.frame_pestanas.guardar_pestana_activa()

    def evento_menu_guardar_como(self):
        if not self.frame_pestanas.hay_pestanas():
            return
        ubicacion = self.mostrar_ventana_guardar_archivo()
        if ubicacion is None:
            return
        self.frame_pestanas.guardar_pestana_activa(ubicacion)

    def evento_menu_cerrar(self):
        if not self.frame_pestanas.hay_pestanas():
            return
        ubicacion, pestana_cerrada = self.frame_pestanas.cerrar_pestana_activa()
        if pestana_cerrada:
            return

        resultado = self.mostrar_dialogo_guardar_cambios(ubicacion)

        if resultado == "no":
            self.frame_pestanas.cerrar_pestana_activa(forzar_cerrar=True)
            return

        archivo_guardado = self.frame_pestanas.guardar_pestana_activa()
        if archivo_guardado is not None:
            self.frame_pestanas.cerrar_pestana_activa()
            return
        ubicacion = self.mostrar_ventana_guardar_archivo()
        if ubicacion is None:
            return
        self.frame_pestanas.guardar_pestana_activa(ubicacion)
        self.frame_pestanas.cerrar_pestana_activa(forzar_cerrar=True)

    def evento_menu_salir(self):
        while self.frame_pestanas.hay_pestanas():
            self.evento_menu_cerrar()
        self.master.destroy()

    # añadir menus
    def agregar_menu_archivo(self, menu_bar):
        fileBar = Menu(menu_bar, tearoff=0)
        fileBar.add_command(label='Abrir', command=self.evento_menu_abrir)
        fileBar.add_command(label='Guardar', command=self.evento_menu_guardar)
        fileBar.add_command(label='Guardar Como', command=self.evento_menu_guardar_como)
        fileBar.add_command(label='Cerrar', command=self.evento_menu_cerrar)
        fileBar.add_command(label='Salir', command=self.evento_menu_salir)
        return fileBar

    # Utils
    def mostrar_ventana_abrir_archivo(self):
        ubicacion = askopenfilename(filetypes=[('Archivos SQL', '*.sql')])
        if ubicacion == '':
            return None
        return ubicacion

    def mostrar_ventana_guardar_archivo(self):
        ubicacion = asksaveasfilename(filetypes=[('Archivos SQL', '*.sql')])
        if ubicacion == '':
            return None
        return ubicacion

    def mostrar_dialogo_guardar_cambios(self,ubicacion=None):
        mensaje = "¿Desde guardar cambios?"
        if ubicacion is not None:
            mensaje += "\nArchivo: "+ubicacion
        return MessageBox.askquestion("Guardar Cambios",mensaje,icon="question")
