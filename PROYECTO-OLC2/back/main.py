from back.utilities.utilities import errors_to_matrix
from grammar import *

def parsear():
    inst = parse("""create data data base use my_db;
                use my_db use;
                select * from my_db;
                insert into my_db (c, d, b) values into(1, "hola");
                if(3, "verdadero",'falso');
                create table tabla1(
                    campo1 int null primary key,
                    campo2 nvarchar null,
                    campo3 date reference tabla2(campo3)
                );

                create procedure procedimiento1(@variable1 as int) as begin 
                    select * from tabla1; 
                end;

                create function funcion1 (@var2 as nvarchar) return date as begin
                    select * from tabla2;
                end;

                exec procedimiento1 'a', 'b';

                while 1 begin
                    select * from tabla2;
                end;

    """)
    if len(errores_sintacticos) > 0 :
        return errors_to_matrix(errores_sintacticos)

parsear()
