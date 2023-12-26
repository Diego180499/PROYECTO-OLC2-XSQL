from src.utilities.utilities import errors_to_matrix
from src.models.symbolTable.SymbolTable import SymbolTable
from src.models.symbolTable.ScopeType import ScopeType
from grammar import *
from src.models.graphviz.Graficador import Graficador


def parsear():

    contenido_1 = '''
    CREATE DATA BASE zapateria;
    DECLARE @today as datetime;
    declare @substring as nchar(10);
    declare @concatenar as nchar(50);
    declare @int as int;
    declare @decimalValue as decimal;
    SELECT tbproducto.id, tbcliente.nombre FROM tbproducto, tbcliente WHERE tbproducto.id == 2;
    set @today = hoy();
    set @concatenar = concatena('hola', ' mundo');
    set @substring = substraer(cas(@today as nchar(100)), 7, 10);
    set @int = cas(cas('1' as decimal) as int);
    set @decimalValue = cas(@concatenar as int) * 10;
    set @today = cas('10-09-2025 05:10:40' as datetime);
    
    create function retorna_valor(@iterador as int) return int as
        begin
        declare @i as int;
        set @i = 0;
        
        while @i < @iterador begin
            set @i = @i + 1;
            
            if @i == 50 then
                return @i;
            end if;
        end;
        
        return @i;
    end;
    
    set @int = exec retorna_valor 10;
    use banco;
    use colegio;
    
    '''

    inst = parse("""
       create data base school;
       
       use school;
       
       create table student(
            id int not null primary key,
            first_name nvarchar(100) not null,
            last_name nvarchar(100) null,
            age int,
            birthday date not null
       );
       
       create table professor(
            id int not null primary key,
            first_name nchar(100) not null,
            age int
       );
       
       create table course(
            id int not null primary key,
            course_name nvarchar(100) not null,
            id_professor int not null reference professor(id)
       );
    """)
    # inst = parse(contenido_1)
    print('Errores sintacticos:')
    if len(errores_sintacticos) > 0:
        print(errors_to_matrix(errores_sintacticos))
        return errors_to_matrix(errores_sintacticos)
    print('Resultado del analisis sintactico:')
    symbol_table = SymbolTable(ScopeType().GLOBAL)
    # Imprecion del ast en formato string
    # print(inst)
    # Generacion del dot para el ast
    graficador = Graficador()
    inst.dot(None, graficador)
    graficador.generarDOT()
    # Ejecucion del codigo
    inst.execute(symbol_table, errores_sintacticos)

    for symbol in symbol_table.symbols:
        print(symbol.id, symbol.variable_type.type, symbol.symbol_type, symbol.value)

parsear()
