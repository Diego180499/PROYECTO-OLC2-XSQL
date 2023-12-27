from src.utilities.utilities import errors_to_matrix, tabla_simbolos_a_matriz
from src.models.symbolTable.SymbolTable import SymbolTable
from src.models.symbolTable.ScopeType import ScopeType
from grammar import *
from src.models.graphviz.Graficador import Graficador


def parsear(contenido):

    resultados_finales = []
    contenido_prueba = ''' use school;        
                select first_name, last_name, age, birthday from student where cas(age as int) < 10;
        '''
    inst = parse(contenido)
    # inst = parse(contenido_1)
    print('Errores sintacticos:')
    if len(errores_sintacticos) > 0:
        print(errors_to_matrix(errores_sintacticos))
        resultados_finales.append([])#0 salida ok select, ejecutar prod almacenado
        resultados_finales.append([])#1 tabla de simbolos
        resultados_finales.append(errors_to_matrix(errores_sintacticos))#2 listado de errores
        resultados_finales.append([])#3 c3e
        return resultados_finales

    print('Resultado del analisis sintactico:')
    symbol_table = SymbolTable(ScopeType().GLOBAL)
    # Imprecion del ast en formato string
    # print(inst)
    # Generacion del dot para el ast
    graficador = Graficador()
    inst.dot(None, graficador)
    graficador.generarDOT()
    # Ejecucion del codigo
    #TODO siempre devolver una lista
    result = inst.execute(symbol_table, errores_sintacticos)
    matriz_tabla_simbolos = tabla_simbolos_a_matriz(symbol_table)
    if isinstance(result,list):
        resultados_finales.append(result)
    else:
        #TODO cuando la salida siempre sea una lista, borrar el else
        resultados_finales.append([])
    resultados_finales.append(matriz_tabla_simbolos)#1 tabla de simbolos
    resultados_finales.append([])#2 errores
    resultados_finales.append([])#3 c3e
    return resultados_finales

#parsear('')
