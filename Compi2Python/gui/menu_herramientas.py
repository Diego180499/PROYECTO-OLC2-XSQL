from tkinter import *
from tkinter import simpledialog, messagebox
from tkinter.filedialog import asksaveasfilename, askopenfilename

from gui.conector import Conector
from src.FILES.manager_db import db_file_manager, db_to_xml
from src.utils.archivo import Archivo
from src.FILES.manager_db.record_file_manager import *
from src.FILES.manager_db.record_file_manager import obtener_contenido_registros_tabla
from src.FILES.import_to_xml_dml import xml_to_records

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
        self.add_command(label='Exportar', image=self.iconos['base-de-datos'], compound="left",
                         command=self.evento_exportar)
        self.add_command(label='Importar', image=self.iconos['sql'], compound="left",
                         command=self.evento_importar)

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
            self.frame_salida.agregar_text_c3d(resultados_finales[3])

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
        self.mostrar_ventana_guardar_archivo_xml(contenido_xml)

    def evento_crear_bbdd(self):
        conector = Conector()

        nombre_bbdd = simpledialog.askstring("Crear Base de Datos",
                                             "Escriba el nombre de la base de datos que desea crear",
                                             parent=self.ventana_principal.ventana)
        if nombre_bbdd is None:
            return
        sentencia_crear_bbdd = "create data base " + nombre_bbdd + ";"
        print("creando bbdd desde ventana:[", sentencia_crear_bbdd, "]")

        resultado = conector.compilar(sentencia_crear_bbdd)

        if resultado[2] is not None and len(resultado[2]) != 0:
            messagebox.showerror("Error", "No se puede crear la base de datos, verifique que no exista")
            return
        messagebox.showinfo("Base de Datos Creada", "La base de datos " + nombre_bbdd + " ha sido creada exitosamente")
        self.evento_actualizar_arbol_bbdd()

    def evento_borrar_bbdd(self):
        conector = Conector()

        nombre_bbdd = simpledialog.askstring("Borrar Base de Datos",
                                             "Escriba el nombre de la base de datos que desea borrar",
                                             parent=self.ventana_principal.ventana)
        if nombre_bbdd is None:
            return

        print("borrando bbdd:[", nombre_bbdd, "]")

        resultado = conector.eliminar_bbdd(nombre_bbdd)
        eliminar_carpeta_registros_db(nombre_bbdd)

        if resultado:
            messagebox.showinfo("Base de Datos Creada",
                                "La base de datos " + nombre_bbdd + " ha sido borrada exitosamente")
            self.evento_actualizar_arbol_bbdd()
            return
        messagebox.showerror("Error", "No se puede borrar la base de datos, verifique que exista")

    def evento_actualizar_arbol_bbdd(self):
        self.frame_arbol.limpiar_arbol()
        self.ventana_principal.__listar_nombres_bd__()

    def evento_importar(self):
        nombre_bbdd = simpledialog.askstring("Importar Tabla","Escriba el nombre de la base de datos a la que desea importar tablas",
        parent=self.ventana_principal.ventana)
        if nombre_bbdd is None:
            return

        if not self.__existe_bbdd__(nombre_bbdd):
            messagebox.showerror("Importar Tabla", f"La base de datos {nombre_bbdd} no existe")
            return

        ubicaciones=[]
        ###llegados aquí es que si exsite bbdd
        while True:
            ubicacion, contenido_archivo=self.abrir_archivo_xml()
            if contenido_archivo is None:
                break

            ubicaciones.append(ubicacion)
            print(contenido_archivo)
            ###Leeemos el contenido del archivo
            ## del contenido sacar el nombrte de la TABLA y ese nombre, se le colocara al archivo importado

            ##con el contenido , creas un nuevo archivo, que se llame como el valor TABLA, dentro de la carpeta
            #llamada igual que el nombre de la bbdd recibida
        message ="Los siguintes archivos han sido importados: "

        registros = []
        for ubicacion in ubicaciones:
            registro = xml_to_records(ubicacion)
            registros.append(registro)


        for registro in registros :
            nombre_tabla = registro.tabla
            for registro_individual in registro.registros :
                insertar_registro(nombre_bbdd,nombre_tabla,registro_individual)
        messagebox.showinfo("¡Se ha importado correctamente!")




    def evento_exportar(self):
        nombre_bbdd_tablas = simpledialog.askstring("Exportar tabla", "Escriba el nombre de la base de datos y el listado de tablas a exportar.\n"
                                                               "Ej. base_de_datos.tabla1,tabla2,...,tablaN",
                                             parent=self.ventana_principal.ventana)
        #TODO validar o limpiar espacios/saltos/tabs

        if nombre_bbdd_tablas is None:
            return
        #print("Base de datos/tablas seleccionadas: ", nombre_bbdd_tablas)

        nombre_bbdd_recibido=nombre_bbdd_tablas.split(".")[0]
        if not self.__existe_bbdd__(nombre_bbdd_recibido):
            messagebox.showerror("Exportar Tabla", f"La base de datos {nombre_bbdd_recibido} no existe")
            return

        tablas = nombre_bbdd_tablas.split(".")[1].split(",")
        tablas_existentes=db_file_manager.obtener_nombres_de_tablas_de_bd(nombre_bbdd_recibido)
        #print(tablas_existentes)
        for tabla in tablas:
            if tabla not in tablas_existentes:
                messagebox.showerror("Exportar Tabla", f'La tabla {tabla} no existe')
                return

        ####### A PARTIR DE AQUI, LAS VALIDACIONES SON CORRECTAS  #######

        for tabla in tablas :
            contenido = obtener_contenido_registros_tabla(nombre_bbdd_recibido, tabla)
            if contenido != None:
                self.mostrar_ventana_guardar_archivo_xml(contenido)
                messagebox.showinfo("Exportar Tabla", f'Se ha exportado correctamente la tabla {tabla}')


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

    def mostrar_ventana_guardar_archivo_xml(self, contenido):
        ubicacion = asksaveasfilename(filetypes=[('Archivos XML', '*.xml')])
        if ubicacion == '':
            return None
        with open(ubicacion, 'w') as archivo:
            archivo.write(contenido)

    def abrir_archivo_xml(self):
        ubicacion = askopenfilename(filetypes=[('Archivos XML', '*.xml')])
        if ubicacion == '':
            return None,None
        try:
            with open(ubicacion, 'r') as archivo:
                self.contenido = archivo.read()
            print("abierto:", ubicacion)
            return ubicacion, self.contenido
        except Exception as e:
            print(str(e))
            return None, None

    def __existe_bbdd__(self,nombre_bbdd_recibido):
        nombres_bbdd=db_file_manager.obtener_nombres_de_bases_de_datos()
        formated_nombres_bbdd=[]
        for nombre_bbdd_de_lista in nombres_bbdd:
            formated_nombres_bbdd.append(nombre_bbdd_de_lista.split(".")[0])
        return nombre_bbdd_recibido in formated_nombres_bbdd
