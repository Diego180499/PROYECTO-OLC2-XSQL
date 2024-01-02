from src.models.code3d.GenC3D import GenC3D
from src.utilities.utilities import errors_to_matrix, tabla_simbolos_a_matriz
from src.models.symbolTable.SymbolTable import SymbolTable
from src.models.symbolTable.ScopeType import ScopeType
from grammar import *
from src.models.graphviz.Graficador import Graficador
from tkinter import messagebox


def parsear(contenido):
    resultados_finales = []
    contenido_prueba = ''' use school;        
                select first_name, last_name, age, birthday from student where cas(age as int) < 10;
        '''
    inst = parse(contenido)
    # inst = parse(contenido_1)
    print('Errores sintacticos:')
    # verificamos si hay errores sintacticos
    if len(errores_sintacticos) > 0:
        print(errors_to_matrix(errores_sintacticos))
        resultados_finales.append([])  # 0 salida ok select, ejecutar prod almacenado
        resultados_finales.append([])  # 1 tabla de simbolos
        resultados_finales.append(errors_to_matrix(errores_sintacticos))  # 2 listado de errores
        resultados_finales.append([])  # 3 c3e
        limpiar_lista_errores()
        return resultados_finales

    # tabla de simbolos
    symbol_table = SymbolTable(ScopeType().GLOBAL)
    # Graficador del AST, ver archivo  ast.dot
    graficador = Graficador()
    inst.dot(None, graficador)
    graficador.generarDOT()
    #Generacion del C3D
    # _______Creamos el generador de C3D_______
    # Generamos una tabla de simbolos para el C3D
    symbol_table_c3d = SymbolTable(ScopeType().GLOBAL)

    generador_c3d = GenC3D()
    inst.c3d(symbol_table_c3d, generador_c3d)
    generador_c3d.write_c3d()
    # _______FIN DE CREACION DEL generador de C3D_______
    # Ejecucion del codigo
    result = inst.execute(symbol_table, errores_sintacticos)  # resultado de la ejecucion
    # verificamos si hay errores semanticos
    if len(errores_sintacticos) > 0:
        print(errors_to_matrix(errores_sintacticos))
        resultados_finales.append([])  # 0 salida ok select, ejecutar prod almacenado
        resultados_finales.append([])  # 1 tabla de simbolos
        resultados_finales.append(errors_to_matrix(errores_sintacticos))  # 2 listado de errores
        resultados_finales.append([])  # 3 c3e
        limpiar_lista_errores()
        return resultados_finales

    matriz_tabla_simbolos = tabla_simbolos_a_matriz(symbol_table)
    if isinstance(result, list):
        resultados_finales.append(result)  # esto es cuando viene un select
    else:
        # TODO cuando la salida siempre sea una lista, borrar el else
        resultados_finales.append([])
    resultados_finales.append(matriz_tabla_simbolos)  # 1 tabla de simbolos
    resultados_finales.append([])  # 2 errores
    resultados_finales.append(generador_c3d.get_code())  # 3 c3e
    messagebox.showinfo("Ejecución Finalizada","Acciones realizadas con exito")
    return resultados_finales

# parsear('')
