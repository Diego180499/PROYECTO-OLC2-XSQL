from utilities.utilities import errors_to_matrix
from symbolTable.SymbolTable import SymbolTable
from grammar import *


def parsear():
    inst = parse("""
    declare @age as int;
    declare @name as nchar(10);
    declare @lastName as nchar(20);
    
    set @age = 20, @name = "Lucía";
    
    if @age < 21 then
        set @name = "Juana";
    else
        set @name = "Patricia";
    end if;
    
    if(@age == 21, 'mayor de edad', 'menor de edad');ç
    
    declare @counter as int;
    set @counter = 10;
    while @counter > 1 begin
        set @counter = @counter - 1;
    end;
    
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
