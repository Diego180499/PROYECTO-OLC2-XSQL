from src.utilities.utilities import errors_to_matrix
from src.models.symbolTable.SymbolTable import SymbolTable
from src.models.symbolTable.ScopeType import ScopeType
from grammar import *
from src.models.graphviz.Graficador import Graficador


def parsear(contenido):

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

    # inst = parse("""
    #    use school;
    #
    #    insert into professor (name, last_name, age, hobby) values ('Luis', 'Munguía', 20);
    # """)
    inst = parse(contenido)

    if len(errores_sintacticos) > 0:
        print(errors_to_matrix(errores_sintacticos))
        matriz_errores = errors_to_matrix(errores_sintacticos)
        limpiar_lista_errores()
        return matriz_errores

    len_matriz = len(obtener_matriz_resultante())
    ### esta matriz se genera si no hay errores sintacticos, pueda que si existan errores semanticos
    ### devuelve tanto errores semanticos como resultados de ejecuciones correctas.
    if len(obtener_matriz_resultante()) > 0:
        matriz_resultado = obtener_matriz_resultante()[len_matriz - 1]
        return matriz_resultado
    print(obtener_db_en_uso())

    symbol_table = SymbolTable()
    for i in inst:
        if i is not None:
            i.execute(symbol_table)

    for symbol in symbol_table.symbols:
        print(symbol.id, symbol.variable_type.type, symbol.symbol_type, symbol.value)

    return [["encabezado"], ["fila"]]

