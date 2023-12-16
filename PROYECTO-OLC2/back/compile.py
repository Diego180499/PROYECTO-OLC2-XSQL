from utilities.utilities import errors_to_matrix
from symbolTable.SymbolTable import SymbolTable
from grammar import *


def parsear():
    inst = parse("""
    select nombre,
        case
        when edad > 18 && edad <= 25
            then 'Adolecente'
        when edad > 25 && edad <= 35
            then 'Adulto joven'
        when edad >35 && edad <= 45
            then 'Adulto Maduro'
        else
            then 'Adulto Mayor'
        end clasificacion
    from tbpersona;
    
    """)
    if len(errores_sintacticos) > 0:
        print(errors_to_matrix(errores_sintacticos))
        return errors_to_matrix(errores_sintacticos)

    symbol_table = SymbolTable()
    for i in inst:
        if i is not None:
            i.execute(symbol_table)

    for symbol in symbol_table.symbols:
        print(symbol.id, symbol.variable_type.type, symbol.symbol_type, symbol.value)


parsear()
