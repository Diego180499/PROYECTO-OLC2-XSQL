from utilities.utilities import errors_to_matrix
from models.symbolTable.SymbolTable import SymbolTable
from models.symbolTable.ScopeType import ScopeType
from grammar import *
from models.graphviz.Graficador import Graficador


def parsear():
    inst = parse("""
    DECLARE @today as datetime;
    declare @substring as nchar(10);
    declare @concatenar as nchar(50);
    declare @int as int;
    declare @decimalValue as decimal;
    
    set @today = hoy();
    set @concatenar = concatena('hola', ' mundo');
    set @substring = substraer(cas(@today as nchar(100)), 7, 10);
    set @int = cas(cas('1' as decimal) as int);
    set @decimalValue = cas(@concatenar as int) * 10;
    set @today = cas('10-09-2025 05:10:40' as datetime);
    
    """)
    print('Errores sintacticos:')
    if len(errores_sintacticos) > 0:
        print(errors_to_matrix(errores_sintacticos))
        return errors_to_matrix(errores_sintacticos)
    print('Resultado del analisis sintactico:')
    symbol_table = SymbolTable(ScopeType().GLOBAL)
    #Impricion del ast en formato string
    #print(inst)
    #Generacion del dot para el ast
    graficador = Graficador()
    inst.dot(None, graficador)
    graficador.generarDOT()
    #Ejecucion del codigo
    inst.execute(symbol_table)

    for symbol in symbol_table.symbols:
        print(symbol.id, symbol.variable_type.type, symbol.symbol_type, symbol.value)


parsear()
