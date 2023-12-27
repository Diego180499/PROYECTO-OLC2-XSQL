from tkinter import RIGHT, Y, X, BOTTOM, Text, BOTH, END
from tkinter.ttk import Notebook, Frame, Label, Scrollbar

from gui.tabla_resultados import TablaResultados


class FrameSalida:

    def __init__(self, ventana_padre, width, height, row, column, rowspan=1, columnspan=1):
        # contenedor de pestañas
        self.notebook = Notebook(ventana_padre, width=width, height=height)
        self.notebook.grid(row=row, column=column, rowspan=rowspan, columnspan=columnspan)

        # pestaña 1
        self.pestana_salida = Frame(self.notebook)
        self.pestana_salida.pack()
        self.tabla_salida = TablaResultados(self.pestana_salida)
        self.notebook.add(self.pestana_salida, text="Salida")
        self.notebook.select(self.pestana_salida)

        # pestaña 2
        self.pestana_simbolos = Frame(self.notebook)
        self.pestana_simbolos.pack()
        self.tabla_simbolos = TablaResultados(self.pestana_simbolos)
        self.notebook.add(self.pestana_simbolos, text="Tabla de Simbolos")
        self.notebook.select(self.pestana_simbolos)

        # pestaña 3
        self.pestana_errores = Frame(self.notebook)
        self.pestana_errores.pack()
        self.tabla_errores = TablaResultados(self.pestana_errores)
        self.notebook.add(self.pestana_errores, text="Errores")
        self.notebook.select(self.pestana_errores)

        # pestaña 4
        self.pestana_c3d = Frame(self.notebook)
        self.pestana_c3d.pack()
        self.notebook.add(self.pestana_c3d, text="Codigo de 3 direcciones")
        self.notebook.select(self.pestana_c3d)

        scrollbar_y = Scrollbar(self.pestana_c3d)
        scrollbar_y.pack(side=RIGHT, fill=Y)
        scrollbar_x = Scrollbar(self.pestana_c3d)
        scrollbar_x.pack(side=BOTTOM, fill=X)
        self.text_c3d = Text(self.pestana_c3d, xscrollcommand=scrollbar_x.set, yscrollcommand=scrollbar_y.set, wrap="none")
        self.text_c3d.pack(fill=BOTH)
        scrollbar_x.config(command=self.text_c3d.xview)
        scrollbar_y.config(command=self.text_c3d.yview)

    def agregar_text_c3d(self,contenido):
        self.text_c3d.insert(END, contenido)

    def limpiar_text_c3d(self):
        self.text_c3d.insert(END, "")

