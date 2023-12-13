from utilities.utilities import errors_to_matrix
from grammar import *


def parsear():
    inst = parse("""create data base my_db;
                use my_db;
                select *, hoy(), concatenar('cadena1', 'TEXTO') from my_db;
                insert into my_db (c, d, b) values (130 * 2 + -4, 1, "hola");
                
                create table tabla1(
                    campo1 int null primary key,
                    campo2 nvarchar null,
                    campo3 date reference tabla2(campo3)
                );

                create procedure procedimiento1(@variable1 as int) as begin 
                    select * from tabla1; 
                    
                    while @contador < @i 
                        begin 
                        set @i= @i+1;
                        select * from usuario;
                        set @i= @i+1;
                    end;
                    
                    if @MONTO > 2000 then
                        set @ISR = @MONTO *0.07;
                        else
                        set @ISR = @MONTO *0.10;
                    end if;
                    
                    case
                        when @edad > 18 && @edad <= 25
                        then 'Adolecente'
                        when @edad > 25 && @edad <= 35
                        then 'Adulto joven'
                        when @edad >35 && @edad <= 45
                        then 'Adulto Maduro'
                        else
                        then 'Adulto Mayor'
                    end
                    
                    
                end;

                create function funcion1 (@var2 as nvarchar) return date as begin
                    select idfactura,nombre,edad from tabla2;
                end;

                exec procedimiento1 'a', 'b';

                while 100 begin
                    select * from tabla2;
                end;

    """)
    if len(errores_sintacticos) > 0:
        print(errors_to_matrix(errores_sintacticos))
        return errors_to_matrix(errores_sintacticos)


parsear()
