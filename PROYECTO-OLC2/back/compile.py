from utilities.utilities import errors_to_matrix
from symbolTable.SymbolTable import SymbolTable
from grammar import *


def parsear():
    inst = parse("""
    declare @nuevaVariable as decimal;
    declare @nuevaVariable2 as int;
    declare @andPrueba as int;
    declare @orPrueba as int;
    set @nuevaVariable = 10 * 5 - 1;
    set @nuevaVariable2 = @nuevaVariable > 200;
    set @andPrueba = 1 && 1;
    set @orPrueba = 111 || 1;
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
