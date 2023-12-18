from utilities.utilities import errors_to_matrix
from models.symbolTable.SymbolTable import SymbolTable
from grammar import *


def parsear():
    inst = parse("""
    create data base banco;

create table products (
product_no int primary key,
name nvarchar(1000),
price decimal not null
);

create table cliente (
id_cliente int primary key,
nombre nvarchar(20) not null ,
apellido nvarchar(20) not null,
tipo_cliente nvarchar(25) not null reference tb_tipo_cliente ( id_tipo_cliente)
);


insert into usuarios (nombre, apellido) values ("Diego",'Estrada');

update tbproducto
set nombreproducto = "Queso", precio = 150 , idunidad = 2
where idproducto == 65;

update tbproducto
set nombreproducto="Queso",precio = 150,descuento = precio*0.10,idunidad = 2
where idproducto == 65;
select * from usuarios;
select usuario.nombre , usuario.apellido, dpi, usuario.nombre from usuario
where dpi == '3137888' && nombre == 'Diego' || apellido == 'Estrada';


create function suma1 (@val1 as int,@val2 as int)
return int
as
begin
declare @valor as int;
set @valor = @val1 + @val2 ;
return @valor;
end;

create procedure pr_nuevoProcedimiento() as begin
declare @variable as decimal;
set @variable = 10.0;
end;

create function pr_nuevaFun() return decimal as begin
declare @variable as decimal;
set @variable = 10.0;
return @variable;
end;

create procedure sp_nuevoprocedimiento(@MONTO as decimal , @IDFACTURA  int)
as
begin
declare @IVA decimal;
declare @ISR decimal;
set @IVA = @MONTO - @MONTO/1.12;
if @MONTO > 2000 then
set @ISR = @MONTO *0.07;
else
set @ISR = @MONTO *0.10;
 end if;
end;

select idfactura,cantidad*price/1.12 iva,cantidad*price*0.07 isr, nit
from tbdetallefactura where fechafactura == '2023-01-01'
&& idproducto == 65;


select nombre,edad, if(edad >= 18,"Mayor de edad", "Menor de Edad") estado
from tbmedico;


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
