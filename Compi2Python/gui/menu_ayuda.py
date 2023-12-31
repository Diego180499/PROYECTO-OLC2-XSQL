from tkinter import *
from tkinter import messagebox as MessageBox
from tkinter.filedialog import askopenfilename, asksaveasfilename

from src.utils.archivo import Archivo


class MenuAyuda(Menu):

    def __init__(self, ventana_principal):
        super().__init__(ventana_principal.menu)
        self.iconos = ventana_principal.iconos
        self.add_command(label='Sobre nosotros', image=self.iconos['informacion'], compound="left",
                         command=self.evento_menu_nostros)

    # eventos barra de menú
    def evento_menu_nostros(self):
        ventana_secundaria = Toplevel()
        ventana_secundaria.title("Sobre nosotros")
        ventana_secundaria.config(width=300, height=200)
        ventana_secundaria.focus()
        ventana_secundaria.resizable(False, False)


        label_usac = Label(ventana_secundaria, image=self.iconos["usac"])
        label_usac.grid(row=1, column=1,columnspan=2)

        label_sistemas = Label(ventana_secundaria, image=self.iconos["sistemas"])
        label_sistemas.grid(row=2, column=1,columnspan=2)

        label_blanco_1 = Label(ventana_secundaria, text="________________________________________________________________")
        label_blanco_1.grid(row=3, column=1,columnspan=2)

        label_nombre_proyecto = Label(ventana_secundaria, text="Proyecto Final", font=("Arial", 25,'bold'))
        label_nombre_proyecto.grid(row=4, column=1,columnspan=2)

        label_curso = Label(ventana_secundaria, text="Organización de Lenguajes y Compiladores 2", font=("Arial", 20))
        label_curso.grid(row=5, column=1,columnspan=2)

        label_blanco_2 = Label(ventana_secundaria, text="")
        label_blanco_2.grid(row=6, column=1,columnspan=2)

        label_alumno_1 = Label(ventana_secundaria, text='Diego Jose Avila Estrada 20000000', font=("Courier New", 20))
        label_alumno_1.grid(row=7, column=1,columnspan=2)

        label_alumno_2 = Label(ventana_secundaria, text='William Alexander Miranda Santos ------', font=("Courier New", 20))
        label_alumno_2.grid(row=8, column=1,columnspan=2)

        label_blanco_3 = Label(ventana_secundaria, text="")
        label_blanco_3.grid(row=9, column=1,columnspan=2)
