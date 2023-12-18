
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'ADD ALTER AND AS ASSIGN BASE BEGIN CAS CASE COLUMN COMMA CONCATENAR CONTAR CREATE DATA DATE DATETIME DECIMAL DECIMAL_VALUE DECLARE DELETE DIVIDE DROP ELSE END EQUALS EXEC FROM FUNCTION GREATER_EQ GREATER_THAN HOY ID IF INSERT INT INTEGER_VALUE INTO KEY LESS_EQ LESS_THAN L_PAREN MINUS NAME NCHAR NOT NOT_EQ NOT_SIGN NULL NVARCHAR OR PLUS POINT PRIMARY PROCEDURE REFERENCE RETURN R_PAREN SELECT SEMICOLON SET STRING SUBSTRAER SUMA TABLE THEN TIMES TRUNCATE UPDATE USE VALUES WHEN WHERE WHILEinit   : statementsstatements : statements statementstatements : statement    : create_database_statement\n                    | use_statement\n                    | declare_statement\n                    | set_statement\n                    | create_table_statement\n                    | select_statement\n                    | insert_statement\n                    | create_function_statement\n                    | create_procedure_statement\n                    | alter_table_statement\n                    | if_statement\n                    | exec_statement\n                    | drop_table_statement\n                    | update_statement\n                    | while_statement\n                    | truncate_statement\n                    | delete_statementcreate_database_statement    : CREATE DATA BASE NAME SEMICOLONuse_statement   : USE NAME SEMICOLONdeclare_statement   : DECLARE ID AS type SEMICOLONdeclare_statement   : DECLARE ID  type SEMICOLONset_statement   : SET assignments SEMICOLONassignments    : assignments COMMA ID ASSIGN aassignments    : ID ASSIGN acreate_table_statement : CREATE TABLE NAME L_PAREN properties R_PAREN SEMICOLONproperties : properties COMMA propertyproperties : propertyproperty   : NAME type null_prod PRIMARY KEYproperty   : NAME type null_prodproperty   : NAME type null_prod REFERENCE NAME L_PAREN NAME R_PARENnull_prod  : NOT NULLnull_prod  : NULLnull_prod  : select_statement   : SELECT columns FROM NAME SEMICOLONselect_statement   : SELECT columns FROM NAME WHERE a SEMICOLONinsert_statement   : INSERT INTO NAME L_PAREN columns R_PAREN VALUES L_PAREN vals R_PAREN SEMICOLONcolumns    : columns COMMA columncolumns    : columns COMMA column POINT columncolumns    : column POINT columncolumns    : columncolumn   : TIMES\n                | NAME\n                | case_statement\n                | if_statement\n                | call_function_prod\n                | a NAMEvals   : vals COMMA avals   : acreate_function_statement  : CREATE FUNCTION NAME L_PAREN parameters R_PAREN RETURN type AS BEGIN statements RETURN a END SEMICOLONcreate_procedure_statement : CREATE PROCEDURE NAME L_PAREN parameters R_PAREN AS BEGIN statements END SEMICOLONparameters : parameters COMMA ID AS typeparameters : parameters COMMA ID typeparameters : ID AS typeparameters : ID  typealter_table_statement  : ALTER TABLE NAME ADD COLUMN NAME type SEMICOLONalter_table_statement  : ALTER TABLE NAME DROP COLUMN NAME SEMICOLONif_statement   : IF a THEN statements END IF SEMICOLONif_statement   : IF a THEN statements ELSE statements END IF SEMICOLONif_statement   : IF L_PAREN a COMMA a COMMA a R_PAREN SEMICOLONif_statement   : IF L_PAREN a COMMA a COMMA a R_PAREN  AS NAMEexec_statement : EXEC NAME vals SEMICOLONdrop_table_statement   : DROP TABLE NAME SEMICOLONupdate_statement   : UPDATE NAME SET column_assignments WHERE a SEMICOLONcolumn_assignments  : column_assignments COMMA NAME ASSIGN acolumn_assignments : NAME ASSIGN awhile_statement    : WHILE a BEGIN statements END SEMICOLONtruncate_statement : TRUNCATE TABLE NAME SEMICOLONdelete_statement : DELETE FROM NAME WHERE a SEMICOLONcase_statement : CASE when_statements END NAMEwhen_statements : WHEN a THEN a when_statementswhen_statements : ELSE THEN atype : INT\n            | DECIMAL\n            | DATE\n            | DATETIMEtype : NCHAR L_PAREN a R_PAREN\n            | NVARCHAR L_PAREN a R_PARENa    : a OR ba  : bb  : b AND cb  : cc  : NOT_SIGN dc  : dd    : d EQUALS e\n            | d NOT_EQ e\n            | d LESS_THAN e\n            | d GREATER_THAN e\n            | d LESS_EQ e\n            | d GREATER_EQ e\n    d  : ee    : e PLUS f\n            | e MINUS fe  : ff    : f TIMES g\n            | f DIVIDE gf  : gg  : MINUS hg  : hh    : INTEGER_VALUEh    : DECIMAL_VALUEh    : STRINGh    : IDh    : NAMEh    : if_statementcall_function_prod   : HOY L_PAREN R_PAREN\n                            | CONCATENAR L_PAREN a COMMA a R_PAREN\n                            | SUBSTRAER L_PAREN a R_PAREN\n                            | CONTAR L_PAREN a R_PAREN\n                            | SUMA L_PAREN a R_PAREN\n                            | CAS L_PAREN a AS type R_PAREN\n    '
    
_lr_action_items = {'CREATE':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,87,96,129,134,142,174,175,177,181,182,184,191,195,210,238,243,244,248,254,260,261,264,272,274,282,284,285,288,291,293,294,295,300,],[-3,21,-2,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,-22,-25,-3,-3,-24,-65,21,-64,21,-70,-21,-23,-37,-3,21,-69,-71,-28,-38,-59,-60,-66,-3,-58,21,-61,-62,-3,-63,21,-53,-39,-52,]),'USE':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,87,96,129,134,142,174,175,177,181,182,184,191,195,210,238,243,244,248,254,260,261,264,272,274,282,284,285,288,291,293,294,295,300,],[-3,22,-2,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,-22,-25,-3,-3,-24,-65,22,-64,22,-70,-21,-23,-37,-3,22,-69,-71,-28,-38,-59,-60,-66,-3,-58,22,-61,-62,-3,-63,22,-53,-39,-52,]),'DECLARE':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,87,96,129,134,142,174,175,177,181,182,184,191,195,210,238,243,244,248,254,260,261,264,272,274,282,284,285,288,291,293,294,295,300,],[-3,23,-2,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,-22,-25,-3,-3,-24,-65,23,-64,23,-70,-21,-23,-37,-3,23,-69,-71,-28,-38,-59,-60,-66,-3,-58,23,-61,-62,-3,-63,23,-53,-39,-52,]),'SET':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,79,87,96,129,134,142,174,175,177,181,182,184,191,195,210,238,243,244,248,254,260,261,264,272,274,282,284,285,288,291,293,294,295,300,],[-3,24,-2,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,133,-22,-25,-3,-3,-24,-65,24,-64,24,-70,-21,-23,-37,-3,24,-69,-71,-28,-38,-59,-60,-66,-3,-58,24,-61,-62,-3,-63,24,-53,-39,-52,]),'SELECT':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,87,96,129,134,142,174,175,177,181,182,184,191,195,210,238,243,244,248,254,260,261,264,272,274,282,284,285,288,291,293,294,295,300,],[-3,25,-2,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,-22,-25,-3,-3,-24,-65,25,-64,25,-70,-21,-23,-37,-3,25,-69,-71,-28,-38,-59,-60,-66,-3,-58,25,-61,-62,-3,-63,25,-53,-39,-52,]),'INSERT':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,87,96,129,134,142,174,175,177,181,182,184,191,195,210,238,243,244,248,254,260,261,264,272,274,282,284,285,288,291,293,294,295,300,],[-3,26,-2,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,-22,-25,-3,-3,-24,-65,26,-64,26,-70,-21,-23,-37,-3,26,-69,-71,-28,-38,-59,-60,-66,-3,-58,26,-61,-62,-3,-63,26,-53,-39,-52,]),'ALTER':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,87,96,129,134,142,174,175,177,181,182,184,191,195,210,238,243,244,248,254,260,261,264,272,274,282,284,285,288,291,293,294,295,300,],[-3,27,-2,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,-22,-25,-3,-3,-24,-65,27,-64,27,-70,-21,-23,-37,-3,27,-69,-71,-28,-38,-59,-60,-66,-3,-58,27,-61,-62,-3,-63,27,-53,-39,-52,]),'IF':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,25,29,32,60,64,75,78,87,96,98,100,102,103,105,108,109,110,111,112,113,115,116,117,118,119,120,121,122,123,124,129,134,142,143,144,153,171,174,175,176,177,178,181,182,183,184,191,194,195,196,197,199,201,209,210,213,214,238,239,243,244,248,254,260,261,262,264,265,272,273,274,282,284,285,288,291,293,294,295,297,300,],[-3,29,-2,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,29,29,29,29,29,29,29,-22,-25,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,-3,-3,-24,29,29,29,29,-65,29,29,-64,29,29,-70,29,-21,-23,29,-37,29,29,29,29,237,-3,29,29,29,29,-69,-71,-28,-38,-59,-60,275,-66,29,-3,29,-58,29,-61,-62,-3,-63,29,-53,-39,29,-52,]),'EXEC':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,87,96,129,134,142,174,175,177,181,182,184,191,195,210,238,243,244,248,254,260,261,264,272,274,282,284,285,288,291,293,294,295,300,],[-3,30,-2,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,-22,-25,-3,-3,-24,-65,30,-64,30,-70,-21,-23,-37,-3,30,-69,-71,-28,-38,-59,-60,-66,-3,-58,30,-61,-62,-3,-63,30,-53,-39,-52,]),'DROP':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,87,96,127,129,134,142,174,175,177,181,182,184,191,195,210,238,243,244,248,254,260,261,264,272,274,282,284,285,288,291,293,294,295,300,],[-3,28,-2,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,-22,-25,173,-3,-3,-24,-65,28,-64,28,-70,-21,-23,-37,-3,28,-69,-71,-28,-38,-59,-60,-66,-3,-58,28,-61,-62,-3,-63,28,-53,-39,-52,]),'UPDATE':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,87,96,129,134,142,174,175,177,181,182,184,191,195,210,238,243,244,248,254,260,261,264,272,274,282,284,285,288,291,293,294,295,300,],[-3,31,-2,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,-22,-25,-3,-3,-24,-65,31,-64,31,-70,-21,-23,-37,-3,31,-69,-71,-28,-38,-59,-60,-66,-3,-58,31,-61,-62,-3,-63,31,-53,-39,-52,]),'WHILE':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,87,96,129,134,142,174,175,177,181,182,184,191,195,210,238,243,244,248,254,260,261,264,272,274,282,284,285,288,291,293,294,295,300,],[-3,32,-2,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,-22,-25,-3,-3,-24,-65,32,-64,32,-70,-21,-23,-37,-3,32,-69,-71,-28,-38,-59,-60,-66,-3,-58,32,-61,-62,-3,-63,32,-53,-39,-52,]),'TRUNCATE':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,87,96,129,134,142,174,175,177,181,182,184,191,195,210,238,243,244,248,254,260,261,264,272,274,282,284,285,288,291,293,294,295,300,],[-3,33,-2,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,-22,-25,-3,-3,-24,-65,33,-64,33,-70,-21,-23,-37,-3,33,-69,-71,-28,-38,-59,-60,-66,-3,-58,33,-61,-62,-3,-63,33,-53,-39,-52,]),'DELETE':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,87,96,129,134,142,174,175,177,181,182,184,191,195,210,238,243,244,248,254,260,261,264,272,274,282,284,285,288,291,293,294,295,300,],[-3,34,-2,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,-22,-25,-3,-3,-24,-65,34,-64,34,-70,-21,-23,-37,-3,34,-69,-71,-28,-38,-59,-60,-66,-3,-58,34,-61,-62,-3,-63,34,-53,-39,-52,]),'$end':([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,87,96,142,174,177,182,184,191,195,243,244,248,254,260,261,264,274,284,285,291,294,295,300,],[-3,0,-1,-2,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,-22,-25,-24,-65,-64,-70,-21,-23,-37,-69,-71,-28,-38,-59,-60,-66,-58,-61,-62,-63,-53,-39,-52,]),'END':([3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,58,59,61,62,63,65,66,67,68,69,70,76,77,87,96,104,114,125,129,134,142,149,160,161,162,163,164,165,166,167,168,169,170,174,175,177,181,182,184,191,195,200,210,238,243,244,248,254,255,260,261,264,272,274,282,284,285,291,294,295,298,300,],[-2,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,-82,-84,-86,-93,-96,-99,-101,-102,-103,-104,-105,-106,-107,-22,-25,151,-85,-100,-3,-3,-24,-81,-83,-87,-88,-89,-90,-91,-92,-94,-95,-97,-98,-65,209,-64,216,-70,-21,-23,-37,-74,-3,262,-69,-71,-28,-38,-73,-59,-60,-66,-3,-58,289,-61,-62,-63,-53,-39,299,-52,]),'ELSE':([3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,51,58,59,61,62,63,65,66,67,68,69,70,76,77,87,96,114,125,129,142,149,160,161,162,163,164,165,166,167,168,169,170,174,175,177,182,184,191,195,231,243,244,248,254,260,261,264,274,284,285,291,294,295,300,],[-2,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,106,-82,-84,-86,-93,-96,-99,-101,-102,-103,-104,-105,-106,-107,-22,-25,-85,-100,-3,-24,-81,-83,-87,-88,-89,-90,-91,-92,-94,-95,-97,-98,-65,210,-64,-70,-21,-23,-37,106,-69,-71,-28,-38,-59,-60,-66,-58,-61,-62,-63,-53,-39,-52,]),'RETURN':([3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,87,96,142,174,177,182,184,191,195,221,243,244,248,254,260,261,264,274,284,285,288,291,293,294,295,300,],[-2,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,-22,-25,-24,-65,-64,-70,-21,-23,-37,250,-69,-71,-28,-38,-59,-60,-66,-58,-61,-62,-3,-63,297,-53,-39,-52,]),'DATA':([21,],[35,]),'TABLE':([21,27,28,33,],[36,72,73,81,]),'FUNCTION':([21,],[37,]),'PROCEDURE':([21,],[38,]),'NAME':([22,25,29,30,31,32,36,37,38,44,45,49,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,75,76,77,78,81,82,83,98,99,100,102,103,105,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,133,138,143,144,149,151,153,160,161,162,163,164,165,166,167,168,169,170,171,176,178,183,194,196,197,199,201,207,208,213,214,215,220,239,261,265,267,273,284,285,286,287,291,297,],[39,44,76,78,79,76,84,85,86,-106,101,-107,-82,-84,76,-86,-93,-96,76,-99,-101,-102,-103,-104,-105,126,127,128,76,-106,-107,76,135,136,137,76,147,44,76,44,76,76,76,76,76,76,76,-85,76,76,76,76,76,76,76,76,76,76,-100,179,185,76,76,-81,198,76,-83,-87,-88,-89,-90,-91,-92,-94,-95,-97,-98,44,76,76,76,76,76,44,76,76,235,236,76,76,242,185,76,-60,76,279,76,-61,-62,291,292,-63,76,]),'ID':([23,24,25,29,32,60,64,75,78,97,98,100,102,103,105,108,109,110,111,112,113,115,116,117,118,119,120,121,122,123,124,139,140,143,144,153,171,176,178,183,194,196,197,199,201,213,214,222,239,265,273,297,],[40,42,70,70,70,70,70,70,70,145,70,70,70,70,70,70,70,70,70,70,70,70,70,70,70,70,70,70,70,70,70,189,189,70,70,70,70,70,70,70,70,70,70,70,70,70,70,251,70,70,70,70,]),'TIMES':([25,44,49,63,65,66,67,68,69,70,76,77,100,103,125,167,168,169,170,171,197,261,284,285,291,],[47,-106,-107,123,-99,-101,-102,-103,-104,-105,-106,-107,47,47,-100,123,123,-97,-98,47,47,-60,-61,-62,-63,]),'CASE':([25,100,103,171,197,],[51,51,51,51,51,]),'HOY':([25,100,103,171,197,],[52,52,52,52,52,]),'CONCATENAR':([25,100,103,171,197,],[53,53,53,53,53,]),'SUBSTRAER':([25,100,103,171,197,],[54,54,54,54,54,]),'CONTAR':([25,100,103,171,197,],[55,55,55,55,55,]),'SUMA':([25,100,103,171,197,],[56,56,56,56,56,]),'CAS':([25,100,103,171,197,],[57,57,57,57,57,]),'NOT_SIGN':([25,29,32,75,78,98,100,102,103,105,108,109,110,111,112,113,143,144,153,171,176,178,183,194,196,197,199,201,213,214,239,265,273,297,],[60,60,60,60,60,60,60,60,60,60,60,60,60,60,60,60,60,60,60,60,60,60,60,60,60,60,60,60,60,60,60,60,60,60,]),'MINUS':([25,29,32,44,49,60,62,63,65,66,67,68,69,70,75,76,77,78,98,100,102,103,105,108,109,110,111,112,113,115,116,117,118,119,120,121,122,123,124,125,143,144,153,161,162,163,164,165,166,167,168,169,170,171,176,178,183,194,196,197,199,201,213,214,239,261,265,273,284,285,291,297,],[64,64,64,-106,-107,64,122,-96,-99,-101,-102,-103,-104,-105,64,-106,-107,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,-100,64,64,64,122,122,122,122,122,122,-94,-95,-97,-98,64,64,64,64,64,64,64,64,64,64,64,64,-60,64,64,-61,-62,-63,64,]),'INTEGER_VALUE':([25,29,32,60,64,75,78,98,100,102,103,105,108,109,110,111,112,113,115,116,117,118,119,120,121,122,123,124,143,144,153,171,176,178,183,194,196,197,199,201,213,214,239,265,273,297,],[67,67,67,67,67,67,67,67,67,67,67,67,67,67,67,67,67,67,67,67,67,67,67,67,67,67,67,67,67,67,67,67,67,67,67,67,67,67,67,67,67,67,67,67,67,67,]),'DECIMAL_VALUE':([25,29,32,60,64,75,78,98,100,102,103,105,108,109,110,111,112,113,115,116,117,118,119,120,121,122,123,124,143,144,153,171,176,178,183,194,196,197,199,201,213,214,239,265,273,297,],[68,68,68,68,68,68,68,68,68,68,68,68,68,68,68,68,68,68,68,68,68,68,68,68,68,68,68,68,68,68,68,68,68,68,68,68,68,68,68,68,68,68,68,68,68,68,]),'STRING':([25,29,32,60,64,75,78,98,100,102,103,105,108,109,110,111,112,113,115,116,117,118,119,120,121,122,123,124,143,144,153,171,176,178,183,194,196,197,199,201,213,214,239,265,273,297,],[69,69,69,69,69,69,69,69,69,69,69,69,69,69,69,69,69,69,69,69,69,69,69,69,69,69,69,69,69,69,69,69,69,69,69,69,69,69,69,69,69,69,69,69,69,69,]),'INTO':([26,],[71,]),'L_PAREN':([29,52,53,54,55,56,57,84,85,86,94,95,126,258,279,],[75,107,108,109,110,111,112,138,139,140,143,144,171,273,287,]),'FROM':([34,43,44,46,47,48,49,50,101,148,150,154,198,202,203,204,230,256,257,261,284,285,291,],[82,99,-45,-43,-44,-46,-47,-48,-49,-40,-42,-108,-72,-110,-111,-112,-41,-109,-113,-60,-61,-62,-63,]),'BASE':([35,],[83,]),'SEMICOLON':([39,41,58,59,61,62,63,65,66,67,68,69,70,76,77,89,90,91,92,93,114,125,128,131,132,135,137,141,146,147,149,160,161,162,163,164,165,166,167,168,169,170,212,216,217,219,226,227,228,229,236,237,241,259,261,275,276,284,285,289,290,291,299,],[87,96,-82,-84,-86,-93,-96,-99,-101,-102,-103,-104,-105,-106,-107,142,-75,-76,-77,-78,-85,-100,174,177,-51,182,184,191,-27,195,-81,-83,-87,-88,-89,-90,-91,-92,-94,-95,-97,-98,-50,243,244,248,-79,-80,-26,254,260,261,264,274,-60,284,285,-61,-62,294,295,-63,300,]),'AS':([40,58,59,61,62,63,65,66,67,68,69,70,76,77,90,91,92,93,114,125,149,159,160,161,162,163,164,165,166,167,168,169,170,189,225,226,227,251,261,269,276,284,285,291,],[88,-82,-84,-86,-93,-96,-99,-101,-102,-103,-104,-105,-106,-107,-75,-76,-77,-78,-85,-100,-81,205,-83,-87,-88,-89,-90,-91,-92,-94,-95,-97,-98,223,253,-79,-80,270,-60,280,286,-61,-62,-63,]),'INT':([40,88,185,189,205,223,235,250,251,270,],[90,90,90,90,90,90,90,90,90,90,]),'DECIMAL':([40,88,185,189,205,223,235,250,251,270,],[91,91,91,91,91,91,91,91,91,91,]),'DATE':([40,88,185,189,205,223,235,250,251,270,],[92,92,92,92,92,92,92,92,92,92,]),'DATETIME':([40,88,185,189,205,223,235,250,251,270,],[93,93,93,93,93,93,93,93,93,93,]),'NCHAR':([40,88,185,189,205,223,235,250,251,270,],[94,94,94,94,94,94,94,94,94,94,]),'NVARCHAR':([40,88,185,189,205,223,235,250,251,270,],[95,95,95,95,95,95,95,95,95,95,]),'COMMA':([41,43,44,46,47,48,49,50,58,59,61,62,63,65,66,67,68,69,70,76,77,90,91,92,93,101,114,125,130,131,132,146,148,149,150,154,155,160,161,162,163,164,165,166,167,168,169,170,180,186,187,188,190,198,202,203,204,206,211,212,218,224,226,227,228,230,240,245,247,249,252,256,257,261,268,271,277,278,281,283,284,285,291,296,],[97,100,-45,-43,-44,-46,-47,-48,-82,-84,-86,-93,-96,-99,-101,-102,-103,-104,-105,-106,-107,-75,-76,-77,-78,-49,-85,-100,176,178,-51,-27,-40,-81,-42,-108,201,-83,-87,-88,-89,-90,-91,-92,-94,-95,-97,-98,215,220,-30,222,222,-72,-110,-111,-112,100,239,-50,-36,-57,-79,-80,-26,-41,-68,-32,-35,-29,-56,-109,-113,-60,-34,-55,-67,-31,-54,178,-61,-62,-63,-33,]),'ASSIGN':([42,145,179,242,],[98,194,213,265,]),'POINT':([44,46,47,48,49,50,101,148,154,198,202,203,204,256,257,261,284,285,291,],[-45,103,-44,-46,-47,-48,-49,197,-108,-72,-110,-111,-112,-109,-113,-60,-61,-62,-63,]),'R_PAREN':([44,46,47,48,49,50,58,59,61,62,63,65,66,67,68,69,70,76,77,90,91,92,93,101,107,114,125,132,148,149,150,154,156,157,158,160,161,162,163,164,165,166,167,168,169,170,186,187,188,190,192,193,198,202,203,204,206,212,218,224,226,227,230,232,233,245,247,249,252,256,257,261,263,268,271,278,281,283,284,285,291,292,296,],[-45,-43,-44,-46,-47,-48,-82,-84,-86,-93,-96,-99,-101,-102,-103,-104,-105,-106,-107,-75,-76,-77,-78,-49,154,-85,-100,-51,-40,-81,-42,-108,202,203,204,-83,-87,-88,-89,-90,-91,-92,-94,-95,-97,-98,219,-30,221,225,226,227,-72,-110,-111,-112,234,-50,-36,-57,-79,-80,-41,256,257,-32,-35,-29,-56,-109,-113,-60,276,-34,-55,-31,-54,290,-61,-62,-63,296,-33,]),'DIVIDE':([44,49,63,65,66,67,68,69,70,76,77,125,167,168,169,170,261,284,285,291,],[-106,-107,124,-99,-101,-102,-103,-104,-105,-106,-107,-100,124,124,-97,-98,-60,-61,-62,-63,]),'PLUS':([44,49,62,63,65,66,67,68,69,70,76,77,125,161,162,163,164,165,166,167,168,169,170,261,284,285,291,],[-106,-107,121,-96,-99,-101,-102,-103,-104,-105,-106,-107,-100,121,121,121,121,121,121,-94,-95,-97,-98,-60,-61,-62,-63,]),'EQUALS':([44,49,61,62,63,65,66,67,68,69,70,76,77,114,125,161,162,163,164,165,166,167,168,169,170,261,284,285,291,],[-106,-107,115,-93,-96,-99,-101,-102,-103,-104,-105,-106,-107,115,-100,-87,-88,-89,-90,-91,-92,-94,-95,-97,-98,-60,-61,-62,-63,]),'NOT_EQ':([44,49,61,62,63,65,66,67,68,69,70,76,77,114,125,161,162,163,164,165,166,167,168,169,170,261,284,285,291,],[-106,-107,116,-93,-96,-99,-101,-102,-103,-104,-105,-106,-107,116,-100,-87,-88,-89,-90,-91,-92,-94,-95,-97,-98,-60,-61,-62,-63,]),'LESS_THAN':([44,49,61,62,63,65,66,67,68,69,70,76,77,114,125,161,162,163,164,165,166,167,168,169,170,261,284,285,291,],[-106,-107,117,-93,-96,-99,-101,-102,-103,-104,-105,-106,-107,117,-100,-87,-88,-89,-90,-91,-92,-94,-95,-97,-98,-60,-61,-62,-63,]),'GREATER_THAN':([44,49,61,62,63,65,66,67,68,69,70,76,77,114,125,161,162,163,164,165,166,167,168,169,170,261,284,285,291,],[-106,-107,118,-93,-96,-99,-101,-102,-103,-104,-105,-106,-107,118,-100,-87,-88,-89,-90,-91,-92,-94,-95,-97,-98,-60,-61,-62,-63,]),'LESS_EQ':([44,49,61,62,63,65,66,67,68,69,70,76,77,114,125,161,162,163,164,165,166,167,168,169,170,261,284,285,291,],[-106,-107,119,-93,-96,-99,-101,-102,-103,-104,-105,-106,-107,119,-100,-87,-88,-89,-90,-91,-92,-94,-95,-97,-98,-60,-61,-62,-63,]),'GREATER_EQ':([44,49,61,62,63,65,66,67,68,69,70,76,77,114,125,161,162,163,164,165,166,167,168,169,170,261,284,285,291,],[-106,-107,120,-93,-96,-99,-101,-102,-103,-104,-105,-106,-107,120,-100,-87,-88,-89,-90,-91,-92,-94,-95,-97,-98,-60,-61,-62,-63,]),'AND':([44,49,58,59,61,62,63,65,66,67,68,69,70,76,77,114,125,149,160,161,162,163,164,165,166,167,168,169,170,261,284,285,291,],[-106,-107,113,-84,-86,-93,-96,-99,-101,-102,-103,-104,-105,-106,-107,-85,-100,113,-83,-87,-88,-89,-90,-91,-92,-94,-95,-97,-98,-60,-61,-62,-63,]),'OR':([44,45,49,58,59,61,62,63,65,66,67,68,69,70,74,76,77,80,114,125,130,132,146,149,152,155,156,157,158,159,160,161,162,163,164,165,166,167,168,169,170,192,193,200,211,212,217,228,229,231,232,240,241,261,263,277,284,285,291,298,],[-106,102,-107,-82,-84,-86,-93,-96,-99,-101,-102,-103,-104,-105,102,-106,-107,102,-85,-100,102,102,102,-81,102,102,102,102,102,102,-83,-87,-88,-89,-90,-91,-92,-94,-95,-97,-98,102,102,102,102,102,102,102,102,102,102,102,102,-60,102,102,-61,-62,-63,102,]),'WHEN':([51,58,59,61,62,63,65,66,67,68,69,70,76,77,114,125,149,160,161,162,163,164,165,166,167,168,169,170,231,261,284,285,291,],[105,-82,-84,-86,-93,-96,-99,-101,-102,-103,-104,-105,-106,-107,-85,-100,-81,-83,-87,-88,-89,-90,-91,-92,-94,-95,-97,-98,105,-60,-61,-62,-63,]),'THEN':([58,59,61,62,63,65,66,67,68,69,70,74,76,77,106,114,125,149,152,160,161,162,163,164,165,166,167,168,169,170,261,284,285,291,],[-82,-84,-86,-93,-96,-99,-101,-102,-103,-104,-105,129,-106,-107,153,-85,-100,-81,199,-83,-87,-88,-89,-90,-91,-92,-94,-95,-97,-98,-60,-61,-62,-63,]),'BEGIN':([58,59,61,62,63,65,66,67,68,69,70,76,77,80,114,125,149,160,161,162,163,164,165,166,167,168,169,170,253,261,280,284,285,291,],[-82,-84,-86,-93,-96,-99,-101,-102,-103,-104,-105,-106,-107,134,-85,-100,-81,-83,-87,-88,-89,-90,-91,-92,-94,-95,-97,-98,272,-60,288,-61,-62,-63,]),'WHERE':([58,59,61,62,63,65,66,67,68,69,70,76,77,114,125,136,147,149,160,161,162,163,164,165,166,167,168,169,170,180,240,261,277,284,285,291,],[-82,-84,-86,-93,-96,-99,-101,-102,-103,-104,-105,-106,-107,-85,-100,183,196,-81,-83,-87,-88,-89,-90,-91,-92,-94,-95,-97,-98,214,-68,-60,-67,-61,-62,-63,]),'NOT':([90,91,92,93,218,226,227,],[-75,-76,-77,-78,246,-79,-80,]),'NULL':([90,91,92,93,218,226,227,246,],[-75,-76,-77,-78,247,-79,-80,268,]),'PRIMARY':([90,91,92,93,218,226,227,245,247,268,],[-75,-76,-77,-78,-36,-79,-80,266,-35,-34,]),'REFERENCE':([90,91,92,93,218,226,227,245,247,268,],[-75,-76,-77,-78,-36,-79,-80,267,-35,-34,]),'ADD':([127,],[172,]),'COLUMN':([172,173,],[207,208,]),'VALUES':([234,],[258,]),'KEY':([266,],[278,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'init':([0,],[1,]),'statements':([0,129,134,210,272,288,],[2,175,181,238,282,293,]),'statement':([2,175,181,238,282,293,],[3,3,3,3,3,3,]),'create_database_statement':([2,175,181,238,282,293,],[4,4,4,4,4,4,]),'use_statement':([2,175,181,238,282,293,],[5,5,5,5,5,5,]),'declare_statement':([2,175,181,238,282,293,],[6,6,6,6,6,6,]),'set_statement':([2,175,181,238,282,293,],[7,7,7,7,7,7,]),'create_table_statement':([2,175,181,238,282,293,],[8,8,8,8,8,8,]),'select_statement':([2,175,181,238,282,293,],[9,9,9,9,9,9,]),'insert_statement':([2,175,181,238,282,293,],[10,10,10,10,10,10,]),'create_function_statement':([2,175,181,238,282,293,],[11,11,11,11,11,11,]),'create_procedure_statement':([2,175,181,238,282,293,],[12,12,12,12,12,12,]),'alter_table_statement':([2,175,181,238,282,293,],[13,13,13,13,13,13,]),'if_statement':([2,25,29,32,60,64,75,78,98,100,102,103,105,108,109,110,111,112,113,115,116,117,118,119,120,121,122,123,124,143,144,153,171,175,176,178,181,183,194,196,197,199,201,213,214,238,239,265,273,282,293,297,],[14,49,77,77,77,77,77,77,77,49,77,49,77,77,77,77,77,77,77,77,77,77,77,77,77,77,77,77,77,77,77,77,49,14,77,77,14,77,77,77,49,77,77,77,77,14,77,77,77,14,14,77,]),'exec_statement':([2,175,181,238,282,293,],[15,15,15,15,15,15,]),'drop_table_statement':([2,175,181,238,282,293,],[16,16,16,16,16,16,]),'update_statement':([2,175,181,238,282,293,],[17,17,17,17,17,17,]),'while_statement':([2,175,181,238,282,293,],[18,18,18,18,18,18,]),'truncate_statement':([2,175,181,238,282,293,],[19,19,19,19,19,19,]),'delete_statement':([2,175,181,238,282,293,],[20,20,20,20,20,20,]),'assignments':([24,],[41,]),'columns':([25,171,],[43,206,]),'a':([25,29,32,75,78,98,100,103,105,108,109,110,111,112,143,144,153,171,176,178,183,194,196,197,199,201,213,214,239,265,273,297,],[45,74,80,130,132,146,45,45,152,155,156,157,158,159,192,193,200,45,211,212,217,228,229,45,231,232,240,241,263,277,132,298,]),'column':([25,100,103,171,197,],[46,148,150,46,230,]),'case_statement':([25,100,103,171,197,],[48,48,48,48,48,]),'call_function_prod':([25,100,103,171,197,],[50,50,50,50,50,]),'b':([25,29,32,75,78,98,100,102,103,105,108,109,110,111,112,143,144,153,171,176,178,183,194,196,197,199,201,213,214,239,265,273,297,],[58,58,58,58,58,58,58,149,58,58,58,58,58,58,58,58,58,58,58,58,58,58,58,58,58,58,58,58,58,58,58,58,58,]),'c':([25,29,32,75,78,98,100,102,103,105,108,109,110,111,112,113,143,144,153,171,176,178,183,194,196,197,199,201,213,214,239,265,273,297,],[59,59,59,59,59,59,59,59,59,59,59,59,59,59,59,160,59,59,59,59,59,59,59,59,59,59,59,59,59,59,59,59,59,59,]),'d':([25,29,32,60,75,78,98,100,102,103,105,108,109,110,111,112,113,143,144,153,171,176,178,183,194,196,197,199,201,213,214,239,265,273,297,],[61,61,61,114,61,61,61,61,61,61,61,61,61,61,61,61,61,61,61,61,61,61,61,61,61,61,61,61,61,61,61,61,61,61,61,]),'e':([25,29,32,60,75,78,98,100,102,103,105,108,109,110,111,112,113,115,116,117,118,119,120,143,144,153,171,176,178,183,194,196,197,199,201,213,214,239,265,273,297,],[62,62,62,62,62,62,62,62,62,62,62,62,62,62,62,62,62,161,162,163,164,165,166,62,62,62,62,62,62,62,62,62,62,62,62,62,62,62,62,62,62,]),'f':([25,29,32,60,75,78,98,100,102,103,105,108,109,110,111,112,113,115,116,117,118,119,120,121,122,143,144,153,171,176,178,183,194,196,197,199,201,213,214,239,265,273,297,],[63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,167,168,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,]),'g':([25,29,32,60,75,78,98,100,102,103,105,108,109,110,111,112,113,115,116,117,118,119,120,121,122,123,124,143,144,153,171,176,178,183,194,196,197,199,201,213,214,239,265,273,297,],[65,65,65,65,65,65,65,65,65,65,65,65,65,65,65,65,65,65,65,65,65,65,65,65,65,169,170,65,65,65,65,65,65,65,65,65,65,65,65,65,65,65,65,65,65,]),'h':([25,29,32,60,64,75,78,98,100,102,103,105,108,109,110,111,112,113,115,116,117,118,119,120,121,122,123,124,143,144,153,171,176,178,183,194,196,197,199,201,213,214,239,265,273,297,],[66,66,66,66,125,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,]),'type':([40,88,185,189,205,223,235,250,251,270,],[89,141,218,224,233,252,259,269,271,281,]),'when_statements':([51,231,],[104,255,]),'vals':([78,273,],[131,283,]),'column_assignments':([133,],[180,]),'properties':([138,],[186,]),'property':([138,220,],[187,249,]),'parameters':([139,140,],[188,190,]),'null_prod':([218,],[245,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> init","S'",1,None,None,None),
  ('init -> statements','init',1,'p_init','grammar.py',218),
  ('statements -> statements statement','statements',2,'p_statements','grammar.py',223),
  ('statements -> <empty>','statements',0,'p_statements_2','grammar.py',229),
  ('statement -> create_database_statement','statement',1,'p_statement','grammar.py',234),
  ('statement -> use_statement','statement',1,'p_statement','grammar.py',235),
  ('statement -> declare_statement','statement',1,'p_statement','grammar.py',236),
  ('statement -> set_statement','statement',1,'p_statement','grammar.py',237),
  ('statement -> create_table_statement','statement',1,'p_statement','grammar.py',238),
  ('statement -> select_statement','statement',1,'p_statement','grammar.py',239),
  ('statement -> insert_statement','statement',1,'p_statement','grammar.py',240),
  ('statement -> create_function_statement','statement',1,'p_statement','grammar.py',241),
  ('statement -> create_procedure_statement','statement',1,'p_statement','grammar.py',242),
  ('statement -> alter_table_statement','statement',1,'p_statement','grammar.py',243),
  ('statement -> if_statement','statement',1,'p_statement','grammar.py',244),
  ('statement -> exec_statement','statement',1,'p_statement','grammar.py',245),
  ('statement -> drop_table_statement','statement',1,'p_statement','grammar.py',246),
  ('statement -> update_statement','statement',1,'p_statement','grammar.py',247),
  ('statement -> while_statement','statement',1,'p_statement','grammar.py',248),
  ('statement -> truncate_statement','statement',1,'p_statement','grammar.py',249),
  ('statement -> delete_statement','statement',1,'p_statement','grammar.py',250),
  ('create_database_statement -> CREATE DATA BASE NAME SEMICOLON','create_database_statement',5,'p_create_database_statement','grammar.py',257),
  ('use_statement -> USE NAME SEMICOLON','use_statement',3,'p_use_statement','grammar.py',263),
  ('declare_statement -> DECLARE ID AS type SEMICOLON','declare_statement',5,'p_declare_statement','grammar.py',269),
  ('declare_statement -> DECLARE ID type SEMICOLON','declare_statement',4,'p_declare_statement_2','grammar.py',273),
  ('set_statement -> SET assignments SEMICOLON','set_statement',3,'p_set_statement','grammar.py',280),
  ('assignments -> assignments COMMA ID ASSIGN a','assignments',5,'p_assignments','grammar.py',285),
  ('assignments -> ID ASSIGN a','assignments',3,'p_assignments_2','grammar.py',291),
  ('create_table_statement -> CREATE TABLE NAME L_PAREN properties R_PAREN SEMICOLON','create_table_statement',7,'p_create_table_statement','grammar.py',299),
  ('properties -> properties COMMA property','properties',3,'p_properties','grammar.py',303),
  ('properties -> property','properties',1,'p_properties_2','grammar.py',307),
  ('property -> NAME type null_prod PRIMARY KEY','property',5,'p_property','grammar.py',311),
  ('property -> NAME type null_prod','property',3,'p_property_2','grammar.py',315),
  ('property -> NAME type null_prod REFERENCE NAME L_PAREN NAME R_PAREN','property',8,'p_property_3','grammar.py',319),
  ('null_prod -> NOT NULL','null_prod',2,'p_null_prod','grammar.py',323),
  ('null_prod -> NULL','null_prod',1,'p_null_prod_2','grammar.py',327),
  ('null_prod -> <empty>','null_prod',0,'p_null_prod_3','grammar.py',331),
  ('select_statement -> SELECT columns FROM NAME SEMICOLON','select_statement',5,'p_select_statement','grammar.py',337),
  ('select_statement -> SELECT columns FROM NAME WHERE a SEMICOLON','select_statement',7,'p_select_statement_2','grammar.py',341),
  ('insert_statement -> INSERT INTO NAME L_PAREN columns R_PAREN VALUES L_PAREN vals R_PAREN SEMICOLON','insert_statement',11,'p_insert_statement','grammar.py',347),
  ('columns -> columns COMMA column','columns',3,'p_columns','grammar.py',353),
  ('columns -> columns COMMA column POINT column','columns',5,'p_columns_2','grammar.py',356),
  ('columns -> column POINT column','columns',3,'p_columns_3','grammar.py',359),
  ('columns -> column','columns',1,'p_columns_4','grammar.py',362),
  ('column -> TIMES','column',1,'p_column','grammar.py',366),
  ('column -> NAME','column',1,'p_column','grammar.py',367),
  ('column -> case_statement','column',1,'p_column','grammar.py',368),
  ('column -> if_statement','column',1,'p_column','grammar.py',369),
  ('column -> call_function_prod','column',1,'p_column','grammar.py',370),
  ('column -> a NAME','column',2,'p_column','grammar.py',371),
  ('vals -> vals COMMA a','vals',3,'p_vals','grammar.py',376),
  ('vals -> a','vals',1,'p_vals_2','grammar.py',380),
  ('create_function_statement -> CREATE FUNCTION NAME L_PAREN parameters R_PAREN RETURN type AS BEGIN statements RETURN a END SEMICOLON','create_function_statement',15,'p_create_function_statement','grammar.py',386),
  ('create_procedure_statement -> CREATE PROCEDURE NAME L_PAREN parameters R_PAREN AS BEGIN statements END SEMICOLON','create_procedure_statement',11,'p_create_procedure_statement','grammar.py',390),
  ('parameters -> parameters COMMA ID AS type','parameters',5,'p_parameters','grammar.py',394),
  ('parameters -> parameters COMMA ID type','parameters',4,'p_parameters_2','grammar.py',397),
  ('parameters -> ID AS type','parameters',3,'p_parameters_3','grammar.py',401),
  ('parameters -> ID type','parameters',2,'p_parameters_4','grammar.py',404),
  ('alter_table_statement -> ALTER TABLE NAME ADD COLUMN NAME type SEMICOLON','alter_table_statement',8,'p_alter_table_statement','grammar.py',410),
  ('alter_table_statement -> ALTER TABLE NAME DROP COLUMN NAME SEMICOLON','alter_table_statement',7,'p_alter_table_statement_2','grammar.py',414),
  ('if_statement -> IF a THEN statements END IF SEMICOLON','if_statement',7,'p_if_statement','grammar.py',427),
  ('if_statement -> IF a THEN statements ELSE statements END IF SEMICOLON','if_statement',9,'p_if_statement_2','grammar.py',432),
  ('if_statement -> IF L_PAREN a COMMA a COMMA a R_PAREN SEMICOLON','if_statement',9,'p_if_statement_3','grammar.py',438),
  ('if_statement -> IF L_PAREN a COMMA a COMMA a R_PAREN AS NAME','if_statement',10,'p_if_statement_4','grammar.py',443),
  ('exec_statement -> EXEC NAME vals SEMICOLON','exec_statement',4,'p_exec_statement','grammar.py',451),
  ('drop_table_statement -> DROP TABLE NAME SEMICOLON','drop_table_statement',4,'p_drop_table_statement','grammar.py',456),
  ('update_statement -> UPDATE NAME SET column_assignments WHERE a SEMICOLON','update_statement',7,'p_update_statement','grammar.py',461),
  ('column_assignments -> column_assignments COMMA NAME ASSIGN a','column_assignments',5,'p_column_assignments','grammar.py',466),
  ('column_assignments -> NAME ASSIGN a','column_assignments',3,'p_column_assignments_2','grammar.py',470),
  ('while_statement -> WHILE a BEGIN statements END SEMICOLON','while_statement',6,'p_while_statement','grammar.py',475),
  ('truncate_statement -> TRUNCATE TABLE NAME SEMICOLON','truncate_statement',4,'p_truncate_statement','grammar.py',481),
  ('delete_statement -> DELETE FROM NAME WHERE a SEMICOLON','delete_statement',6,'p_delete_statement','grammar.py',486),
  ('case_statement -> CASE when_statements END NAME','case_statement',4,'p_case_statement','grammar.py',491),
  ('when_statements -> WHEN a THEN a when_statements','when_statements',5,'p_when_statement','grammar.py',495),
  ('when_statements -> ELSE THEN a','when_statements',3,'p_when_statement_2','grammar.py',499),
  ('type -> INT','type',1,'p_type','grammar.py',503),
  ('type -> DECIMAL','type',1,'p_type','grammar.py',504),
  ('type -> DATE','type',1,'p_type','grammar.py',505),
  ('type -> DATETIME','type',1,'p_type','grammar.py',506),
  ('type -> NCHAR L_PAREN a R_PAREN','type',4,'p_type_2','grammar.py',512),
  ('type -> NVARCHAR L_PAREN a R_PAREN','type',4,'p_type_2','grammar.py',513),
  ('a -> a OR b','a',3,'p_a','grammar.py',517),
  ('a -> b','a',1,'p_a_2','grammar.py',522),
  ('b -> b AND c','b',3,'p_b','grammar.py',527),
  ('b -> c','b',1,'p_b_2','grammar.py',532),
  ('c -> NOT_SIGN d','c',2,'p_c','grammar.py',537),
  ('c -> d','c',1,'p_c_2','grammar.py',542),
  ('d -> d EQUALS e','d',3,'p_d','grammar.py',547),
  ('d -> d NOT_EQ e','d',3,'p_d','grammar.py',548),
  ('d -> d LESS_THAN e','d',3,'p_d','grammar.py',549),
  ('d -> d GREATER_THAN e','d',3,'p_d','grammar.py',550),
  ('d -> d LESS_EQ e','d',3,'p_d','grammar.py',551),
  ('d -> d GREATER_EQ e','d',3,'p_d','grammar.py',552),
  ('d -> e','d',1,'p_d_2','grammar.py',558),
  ('e -> e PLUS f','e',3,'p_e','grammar.py',563),
  ('e -> e MINUS f','e',3,'p_e','grammar.py',564),
  ('e -> f','e',1,'p_e_2','grammar.py',569),
  ('f -> f TIMES g','f',3,'p_f','grammar.py',574),
  ('f -> f DIVIDE g','f',3,'p_f','grammar.py',575),
  ('f -> g','f',1,'p_f_2','grammar.py',580),
  ('g -> MINUS h','g',2,'p_g','grammar.py',585),
  ('g -> h','g',1,'p_g_2','grammar.py',590),
  ('h -> INTEGER_VALUE','h',1,'p_h','grammar.py',595),
  ('h -> DECIMAL_VALUE','h',1,'p_h_2','grammar.py',600),
  ('h -> STRING','h',1,'p_h_3','grammar.py',605),
  ('h -> ID','h',1,'p_h_4','grammar.py',610),
  ('h -> NAME','h',1,'p_h_5','grammar.py',615),
  ('h -> if_statement','h',1,'p_h_6','grammar.py',619),
  ('call_function_prod -> HOY L_PAREN R_PAREN','call_function_prod',3,'p_call_function_prod','grammar.py',623),
  ('call_function_prod -> CONCATENAR L_PAREN a COMMA a R_PAREN','call_function_prod',6,'p_call_function_prod','grammar.py',624),
  ('call_function_prod -> SUBSTRAER L_PAREN a R_PAREN','call_function_prod',4,'p_call_function_prod','grammar.py',625),
  ('call_function_prod -> CONTAR L_PAREN a R_PAREN','call_function_prod',4,'p_call_function_prod','grammar.py',626),
  ('call_function_prod -> SUMA L_PAREN a R_PAREN','call_function_prod',4,'p_call_function_prod','grammar.py',627),
  ('call_function_prod -> CAS L_PAREN a AS type R_PAREN','call_function_prod',6,'p_call_function_prod','grammar.py',628),
]
