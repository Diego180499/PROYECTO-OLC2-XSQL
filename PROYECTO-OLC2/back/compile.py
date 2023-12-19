from utilities.utilities import errors_to_matrix
from models.symbolTable.SymbolTable import SymbolTable
from models.symbolTable.ScopeType import ScopeType
from grammar import *


def parsear():
    inst = parse("""
    declare @message as nvarchar(100);
    declare @hello as nvarchar(5);
    
    create function isAnAdult(@age as int) return nchar(50) as
        begin
        if @age > 17 then
            return 'mayor';
        else
            return 'menor';
        end if;
    end;
    
    create function hello() return int as
        begin
        return 'hello';
    end;
    
    set @hello = exec hello;
    set @message = exec isAnAdult 20;
    """)
    print('Errores sintacticos:')
    if len(errores_sintacticos) > 0:
        print(errors_to_matrix(errores_sintacticos))
        return errors_to_matrix(errores_sintacticos)
    print('Resultado del analisis sintactico:')
    symbol_table = SymbolTable(ScopeType().GLOBAL)
    for i in inst:
        if i is not None:
            print(i)
            #i.execute(symbol_table)

    for symbol in symbol_table.symbols:
        print(symbol.id, symbol.variable_type.type, symbol.symbol_type, symbol.value)


parsear()
