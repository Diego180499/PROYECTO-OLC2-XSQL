
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'ADD ALTER AND AS ASSIGN BASE BEGIN BIT CAS CASE COLUMN COMMA CONCATENAR CONTAR CREATE DATA DATE DATETIME DECIMAL DECIMAL_VALUE DECLARE DELETE DIVIDE DROP ELSE END EQUALS EXEC FROM FUNCTION GREATER_EQ GREATER_THAN HOY ID IF INSERT INT INTEGER_VALUE INTO KEY LESS_EQ LESS_THAN L_PAREN MINUS NAME NCHAR NOT NOT_EQ NOT_SIGN NULL NVARCHAR OR PLUS PRIMARY PROCEDURE REFERENCE RETURN R_PAREN SELECT SEMICOLON SET STRING SUBSTRAER SUMA TABLE THEN TIMES TRUNCATE UPDATE USE VALUES WHEN WHERE WHILEinit   : statementsstatements : statements statementstatements : statement    : create_database_statement\n                    | use_statement\n                    | declare_statement\n                    | set_statement\n                    | create_table_statement\n                    | select_statement\n                    | insert_statement\n                    | create_function_statement\n                    | create_procedure_statement\n                    | alter_table_statement\n                    | if_statement\n                    | exec_statement\n                    | drop_table_statement\n                    | case_statement\n                    | update_statement\n                    | while_statement\n                    | truncate_statement\n                    | delete_statementcreate_database_statement    : CREATE DATA BASE NAME SEMICOLONuse_statement   : USE NAME SEMICOLONdeclare_statement   : DECLARE ID AS type SEMICOLONset_statement   : SET assignments SEMICOLONassignments    : assignments COMMA ID ASSIGN aassignments    : ID ASSIGN acreate_table_statement : CREATE TABLE NAME L_PAREN properties R_PAREN SEMICOLONproperties : properties COMMA propertyproperties : propertyproperty   : NAME type null_prod PRIMARY KEYproperty   : NAME type null_prodproperty   : NAME type null_prod REFERENCE NAME L_PAREN NAME R_PARENnull_prod  : NOT NULLnull_prod  : NULLnull_prod  : select_statement   : SELECT columns FROM NAME SEMICOLONselect_statement   : SELECT columns FROM NAME WHERE a SEMICOLONinsert_statement   : INSERT INTO NAME L_PAREN columns R_PAREN VALUES L_PAREN vals R_PAREN SEMICOLONcolumns    : columns COMMA columncolumns    : columncolumn   : TIMES\n                | NAME\n                | call_function_prodvals   : vals COMMA avals   : acreate_function_statement  : CREATE FUNCTION NAME L_PAREN parameters R_PAREN RETURN type AS BEGIN statements END SEMICOLONcreate_procedure_statement : CREATE PROCEDURE NAME L_PAREN parameters R_PAREN AS BEGIN statements END SEMICOLONparameters : parameters COMMA ID AS typeparameters : ID AS typealter_table_statement  : ALTER TABLE NAME ADD COLUMN NAME type SEMICOLONalter_table_statement  : ALTER TABLE NAME DROP COLUMN NAME SEMICOLONif_statement   : IF a THEN statement END IF SEMICOLONif_statement   : IF a THEN statement ELSE statement END IF SEMICOLONif_statement   : IF L_PAREN a COMMA a COMMA a R_PAREN SEMICOLONexec_statement : EXEC NAME vals SEMICOLONdrop_table_statement   : DROP TABLE NAME SEMICOLONupdate_statement   : UPDATE NAME SET column_assignments WHERE a SEMICOLONcolumn_assignments  : column_assignments COMMA NAME ASSIGN acolumn_assignments : NAME ASSIGN awhile_statement    : WHILE a BEGIN statements END SEMICOLONtruncate_statement : TRUNCATE TABLE NAME SEMICOLONdelete_statement : DELETE FROM NAME WHERE a SEMICOLONcase_statement : CASE WHEN a THEN a when_statement ELSE THEN a ENDwhen_statement : WHEN a THEN a when_statementwhen_statement : type : INT\n            | DECIMAL\n            | BIT\n            | NCHAR\n            | NVARCHAR\n            | DATE\n            | DATETIMEa    : a OR ba  : bb  : b AND cb  : cc  : NOT_SIGN dc  : dd    : d EQUALS e\n            | d NOT_EQ e\n            | d LESS_THAN e\n            | d GREATER_THAN e\n            | d LESS_EQ e\n            | d GREATER_EQ e\n    d  : ee    : e PLUS f\n            | e MINUS fe  : ff    : f TIMES g\n            | f DIVIDE gf  : gg  : MINUS hg  : hh    : INTEGER_VALUE\n            | DECIMAL_VALUE\n            | STRING\n            | IDcall_function_prod   : HOY L_PAREN R_PAREN\n                            | CONCATENAR L_PAREN a COMMA a R_PAREN\n                            | SUBSTRAER L_PAREN a R_PAREN\n                            | CONTAR L_PAREN a R_PAREN\n                            | SUMA L_PAREN a R_PAREN\n                            | CAS L_PAREN a AS type R_PAREN\n    '
    
_lr_action_items = {'CREATE':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,84,86,100,120,148,163,168,169,171,178,180,191,222,223,227,233,238,239,244,251,253,263,265,266,270,274,276,277,278,281,],[-3,22,-2,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,-21,-23,-25,22,-3,-57,-56,22,-62,-22,-24,-37,22,-61,-63,-28,-38,-52,-53,-58,-3,-51,22,-54,-55,-3,-64,22,-48,-39,-47,]),'USE':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,84,86,100,120,148,163,168,169,171,178,180,191,222,223,227,233,238,239,244,251,253,263,265,266,270,274,276,277,278,281,],[-3,23,-2,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,-21,-23,-25,23,-3,-57,-56,23,-62,-22,-24,-37,23,-61,-63,-28,-38,-52,-53,-58,-3,-51,23,-54,-55,-3,-64,23,-48,-39,-47,]),'DECLARE':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,84,86,100,120,148,163,168,169,171,178,180,191,222,223,227,233,238,239,244,251,253,263,265,266,270,274,276,277,278,281,],[-3,24,-2,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,-21,-23,-25,24,-3,-57,-56,24,-62,-22,-24,-37,24,-61,-63,-28,-38,-52,-53,-58,-3,-51,24,-54,-55,-3,-64,24,-48,-39,-47,]),'SET':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,76,84,86,100,120,148,163,168,169,171,178,180,191,222,223,227,233,238,239,244,251,253,263,265,266,270,274,276,277,278,281,],[-3,25,-2,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,-21,119,-23,-25,25,-3,-57,-56,25,-62,-22,-24,-37,25,-61,-63,-28,-38,-52,-53,-58,-3,-51,25,-54,-55,-3,-64,25,-48,-39,-47,]),'SELECT':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,84,86,100,120,148,163,168,169,171,178,180,191,222,223,227,233,238,239,244,251,253,263,265,266,270,274,276,277,278,281,],[-3,26,-2,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,-21,-23,-25,26,-3,-57,-56,26,-62,-22,-24,-37,26,-61,-63,-28,-38,-52,-53,-58,-3,-51,26,-54,-55,-3,-64,26,-48,-39,-47,]),'INSERT':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,84,86,100,120,148,163,168,169,171,178,180,191,222,223,227,233,238,239,244,251,253,263,265,266,270,274,276,277,278,281,],[-3,27,-2,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,-21,-23,-25,27,-3,-57,-56,27,-62,-22,-24,-37,27,-61,-63,-28,-38,-52,-53,-58,-3,-51,27,-54,-55,-3,-64,27,-48,-39,-47,]),'ALTER':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,84,86,100,120,148,163,168,169,171,178,180,191,222,223,227,233,238,239,244,251,253,263,265,266,270,274,276,277,278,281,],[-3,28,-2,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,-21,-23,-25,28,-3,-57,-56,28,-62,-22,-24,-37,28,-61,-63,-28,-38,-52,-53,-58,-3,-51,28,-54,-55,-3,-64,28,-48,-39,-47,]),'IF':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,84,86,100,120,148,163,168,169,171,178,180,190,191,222,223,227,233,238,239,240,244,251,253,263,265,266,270,274,276,277,278,281,],[-3,30,-2,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,-21,-23,-25,30,-3,-57,-56,30,-62,-22,-24,-37,214,30,-61,-63,-28,-38,-52,-53,254,-58,-3,-51,30,-54,-55,-3,-64,30,-48,-39,-47,]),'EXEC':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,84,86,100,120,148,163,168,169,171,178,180,191,222,223,227,233,238,239,244,251,253,263,265,266,270,274,276,277,278,281,],[-3,31,-2,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,-21,-23,-25,31,-3,-57,-56,31,-62,-22,-24,-37,31,-61,-63,-28,-38,-52,-53,-58,-3,-51,31,-54,-55,-3,-64,31,-48,-39,-47,]),'DROP':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,84,86,98,100,120,148,163,168,169,171,178,180,191,222,223,227,233,238,239,244,251,253,263,265,266,270,274,276,277,278,281,],[-3,29,-2,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,-21,-23,-25,147,29,-3,-57,-56,29,-62,-22,-24,-37,29,-61,-63,-28,-38,-52,-53,-58,-3,-51,29,-54,-55,-3,-64,29,-48,-39,-47,]),'CASE':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,84,86,100,120,148,163,168,169,171,178,180,191,222,223,227,233,238,239,244,251,253,263,265,266,270,274,276,277,278,281,],[-3,32,-2,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,-21,-23,-25,32,-3,-57,-56,32,-62,-22,-24,-37,32,-61,-63,-28,-38,-52,-53,-58,-3,-51,32,-54,-55,-3,-64,32,-48,-39,-47,]),'UPDATE':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,84,86,100,120,148,163,168,169,171,178,180,191,222,223,227,233,238,239,244,251,253,263,265,266,270,274,276,277,278,281,],[-3,33,-2,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,-21,-23,-25,33,-3,-57,-56,33,-62,-22,-24,-37,33,-61,-63,-28,-38,-52,-53,-58,-3,-51,33,-54,-55,-3,-64,33,-48,-39,-47,]),'WHILE':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,84,86,100,120,148,163,168,169,171,178,180,191,222,223,227,233,238,239,244,251,253,263,265,266,270,274,276,277,278,281,],[-3,34,-2,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,-21,-23,-25,34,-3,-57,-56,34,-62,-22,-24,-37,34,-61,-63,-28,-38,-52,-53,-58,-3,-51,34,-54,-55,-3,-64,34,-48,-39,-47,]),'TRUNCATE':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,84,86,100,120,148,163,168,169,171,178,180,191,222,223,227,233,238,239,244,251,253,263,265,266,270,274,276,277,278,281,],[-3,35,-2,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,-21,-23,-25,35,-3,-57,-56,35,-62,-22,-24,-37,35,-61,-63,-28,-38,-52,-53,-58,-3,-51,35,-54,-55,-3,-64,35,-48,-39,-47,]),'DELETE':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,84,86,100,120,148,163,168,169,171,178,180,191,222,223,227,233,238,239,244,251,253,263,265,266,270,274,276,277,278,281,],[-3,36,-2,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,-21,-23,-25,36,-3,-57,-56,36,-62,-22,-24,-37,36,-61,-63,-28,-38,-52,-53,-58,-3,-51,36,-54,-55,-3,-64,36,-48,-39,-47,]),'$end':([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,84,86,148,163,169,171,178,180,222,223,227,233,238,239,244,253,265,266,274,277,278,281,],[-3,0,-1,-2,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,-21,-23,-25,-57,-56,-62,-22,-24,-37,-61,-63,-28,-38,-52,-53,-58,-51,-54,-55,-64,-48,-39,-47,]),'END':([3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,61,62,64,65,66,68,69,70,71,72,73,84,86,104,115,120,148,149,150,152,153,154,155,156,157,158,159,160,161,162,163,168,169,171,178,180,215,222,223,227,233,238,239,244,251,253,263,265,266,268,270,274,276,277,278,281,],[-2,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,-21,-75,-77,-79,-86,-89,-92,-94,-95,-96,-97,-98,-23,-25,-78,-93,-3,-57,190,-74,-76,-80,-81,-82,-83,-84,-85,-87,-88,-90,-91,-56,198,-62,-22,-24,-37,240,-61,-63,-28,-38,-52,-53,-58,-3,-51,271,-54,-55,274,-3,-64,280,-48,-39,-47,]),'ELSE':([4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,61,62,64,65,66,68,69,70,71,72,73,84,86,104,115,148,149,150,152,153,154,155,156,157,158,159,160,161,162,163,169,171,178,180,194,218,222,223,227,233,238,239,244,253,265,266,267,273,274,277,278,281,],[-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,-21,-75,-77,-79,-86,-89,-92,-94,-95,-96,-97,-98,-23,-25,-78,-93,-57,191,-74,-76,-80,-81,-82,-83,-84,-85,-87,-88,-90,-91,-56,-62,-22,-24,-37,-66,243,-61,-63,-28,-38,-52,-53,-58,-51,-54,-55,-66,-65,-64,-48,-39,-47,]),'DATA':([22,],[37,]),'TABLE':([22,28,29,35,],[38,57,58,78,]),'FUNCTION':([22,],[39,]),'PROCEDURE':([22,],[40,]),'NAME':([23,26,31,33,38,39,40,56,57,58,78,79,80,89,90,119,124,145,188,189,197,202,247,269,],[41,46,74,76,81,82,83,97,98,99,121,122,123,137,46,166,172,46,212,213,221,172,260,275,]),'ID':([24,25,30,34,60,63,67,74,75,87,88,92,93,94,95,96,101,103,105,106,107,108,109,110,111,112,113,114,125,126,151,164,165,170,179,181,182,195,196,204,216,217,245,252,256,257,],[42,44,73,73,73,73,73,73,73,135,73,73,73,73,73,73,73,73,73,73,73,73,73,73,73,73,73,73,176,176,73,73,73,73,73,73,73,73,73,230,73,73,73,73,73,73,]),'TIMES':([26,66,68,69,70,71,72,73,90,115,145,159,160,161,162,],[48,113,-92,-94,-95,-96,-97,-98,48,-93,48,113,113,-90,-91,]),'HOY':([26,90,145,],[50,50,50,]),'CONCATENAR':([26,90,145,],[51,51,51,]),'SUBSTRAER':([26,90,145,],[52,52,52,]),'CONTAR':([26,90,145,],[53,53,53,]),'SUMA':([26,90,145,],[54,54,54,]),'CAS':([26,90,145,],[55,55,55,]),'INTO':([27,],[56,]),'L_PAREN':([30,50,51,52,53,54,55,81,82,83,97,236,260,],[60,91,92,93,94,95,96,124,125,126,145,252,269,]),'NOT_SIGN':([30,34,60,74,75,88,92,93,94,95,96,101,103,151,164,165,170,179,181,182,195,196,216,217,245,252,256,257,],[63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,]),'MINUS':([30,34,60,63,65,66,68,69,70,71,72,73,74,75,88,92,93,94,95,96,101,103,105,106,107,108,109,110,111,112,113,114,115,151,153,154,155,156,157,158,159,160,161,162,164,165,170,179,181,182,195,196,216,217,245,252,256,257,],[67,67,67,67,112,-89,-92,-94,-95,-96,-97,-98,67,67,67,67,67,67,67,67,67,67,67,67,67,67,67,67,67,67,67,67,-93,67,112,112,112,112,112,112,-87,-88,-90,-91,67,67,67,67,67,67,67,67,67,67,67,67,67,67,]),'INTEGER_VALUE':([30,34,60,63,67,74,75,88,92,93,94,95,96,101,103,105,106,107,108,109,110,111,112,113,114,151,164,165,170,179,181,182,195,196,216,217,245,252,256,257,],[70,70,70,70,70,70,70,70,70,70,70,70,70,70,70,70,70,70,70,70,70,70,70,70,70,70,70,70,70,70,70,70,70,70,70,70,70,70,70,70,]),'DECIMAL_VALUE':([30,34,60,63,67,74,75,88,92,93,94,95,96,101,103,105,106,107,108,109,110,111,112,113,114,151,164,165,170,179,181,182,195,196,216,217,245,252,256,257,],[71,71,71,71,71,71,71,71,71,71,71,71,71,71,71,71,71,71,71,71,71,71,71,71,71,71,71,71,71,71,71,71,71,71,71,71,71,71,71,71,]),'STRING':([30,34,60,63,67,74,75,88,92,93,94,95,96,101,103,105,106,107,108,109,110,111,112,113,114,151,164,165,170,179,181,182,195,196,216,217,245,252,256,257,],[72,72,72,72,72,72,72,72,72,72,72,72,72,72,72,72,72,72,72,72,72,72,72,72,72,72,72,72,72,72,72,72,72,72,72,72,72,72,72,72,]),'WHEN':([32,61,62,64,65,66,68,69,70,71,72,73,104,115,150,152,153,154,155,156,157,158,159,160,161,162,194,267,],[75,-75,-77,-79,-86,-89,-92,-94,-95,-96,-97,-98,-78,-93,-74,-76,-80,-81,-82,-83,-84,-85,-87,-88,-90,-91,217,217,]),'FROM':([36,45,46,47,48,49,138,139,183,184,185,234,235,],[79,89,-43,-41,-42,-44,-40,-99,-101,-102,-103,-100,-104,]),'BASE':([37,],[80,]),'SEMICOLON':([41,43,61,62,64,65,66,68,69,70,71,72,73,99,104,115,116,117,121,123,127,128,129,130,131,132,133,134,136,137,150,152,153,154,155,156,157,158,159,160,161,162,193,198,199,201,207,208,213,214,220,237,254,255,271,272,280,],[84,86,-75,-77,-79,-86,-89,-92,-94,-95,-96,-97,-98,148,-78,-93,163,-46,169,171,178,-67,-68,-69,-70,-71,-72,-73,-27,180,-74,-76,-80,-81,-82,-83,-84,-85,-87,-88,-90,-91,-45,222,223,227,-26,233,238,239,244,253,265,266,277,278,281,]),'AS':([42,61,62,64,65,66,68,69,70,71,72,73,104,115,128,129,130,131,132,133,134,144,150,152,153,154,155,156,157,158,159,160,161,162,176,206,230,249,],[85,-75,-77,-79,-86,-89,-92,-94,-95,-96,-97,-98,-78,-93,-67,-68,-69,-70,-71,-72,-73,186,-74,-76,-80,-81,-82,-83,-84,-85,-87,-88,-90,-91,205,232,250,261,]),'COMMA':([43,45,46,47,48,49,61,62,64,65,66,68,69,70,71,72,73,102,104,115,116,117,128,129,130,131,132,133,134,136,138,139,140,150,152,153,154,155,156,157,158,159,160,161,162,167,173,174,175,177,183,184,185,187,192,193,200,207,219,224,226,228,231,234,235,248,258,259,262,264,279,],[87,90,-43,-41,-42,-44,-75,-77,-79,-86,-89,-92,-94,-95,-96,-97,-98,151,-78,-93,164,-46,-67,-68,-69,-70,-71,-72,-73,-27,-40,-99,182,-74,-76,-80,-81,-82,-83,-84,-85,-87,-88,-90,-91,197,202,-30,204,204,-101,-102,-103,90,216,-45,-36,-26,-60,-32,-35,-29,-50,-100,-104,-34,-59,-31,-49,164,-33,]),'ASSIGN':([44,135,166,221,],[88,179,195,245,]),'R_PAREN':([46,47,48,49,61,62,64,65,66,68,69,70,71,72,73,91,104,115,117,128,129,130,131,132,133,134,138,139,141,142,143,150,152,153,154,155,156,157,158,159,160,161,162,173,174,175,177,183,184,185,187,193,200,209,210,224,226,228,231,234,235,241,248,259,262,264,275,279,],[-43,-41,-42,-44,-75,-77,-79,-86,-89,-92,-94,-95,-96,-97,-98,139,-78,-93,-46,-67,-68,-69,-70,-71,-72,-73,-40,-99,183,184,185,-74,-76,-80,-81,-82,-83,-84,-85,-87,-88,-90,-91,201,-30,203,206,-101,-102,-103,211,-45,-36,234,235,-32,-35,-29,-50,-100,-104,255,-34,-31,-49,272,279,-33,]),'THEN':([59,61,62,64,65,66,68,69,70,71,72,73,104,115,118,150,152,153,154,155,156,157,158,159,160,161,162,242,243,],[100,-75,-77,-79,-86,-89,-92,-94,-95,-96,-97,-98,-78,-93,165,-74,-76,-80,-81,-82,-83,-84,-85,-87,-88,-90,-91,256,257,]),'OR':([59,61,62,64,65,66,68,69,70,71,72,73,77,102,104,115,117,118,136,140,141,142,143,144,150,152,153,154,155,156,157,158,159,160,161,162,192,193,194,199,207,208,209,219,220,241,242,258,267,268,],[101,-75,-77,-79,-86,-89,-92,-94,-95,-96,-97,-98,101,101,-78,-93,101,101,101,101,101,101,101,101,-74,-76,-80,-81,-82,-83,-84,-85,-87,-88,-90,-91,101,101,101,101,101,101,101,101,101,101,101,101,101,101,]),'BEGIN':([61,62,64,65,66,68,69,70,71,72,73,77,104,115,150,152,153,154,155,156,157,158,159,160,161,162,232,261,],[-75,-77,-79,-86,-89,-92,-94,-95,-96,-97,-98,120,-78,-93,-74,-76,-80,-81,-82,-83,-84,-85,-87,-88,-90,-91,251,270,]),'WHERE':([61,62,64,65,66,68,69,70,71,72,73,104,115,122,137,150,152,153,154,155,156,157,158,159,160,161,162,167,219,258,],[-75,-77,-79,-86,-89,-92,-94,-95,-96,-97,-98,-78,-93,170,181,-74,-76,-80,-81,-82,-83,-84,-85,-87,-88,-90,-91,196,-60,-59,]),'AND':([61,62,64,65,66,68,69,70,71,72,73,104,115,150,152,153,154,155,156,157,158,159,160,161,162,],[103,-77,-79,-86,-89,-92,-94,-95,-96,-97,-98,-78,-93,103,-76,-80,-81,-82,-83,-84,-85,-87,-88,-90,-91,]),'EQUALS':([64,65,66,68,69,70,71,72,73,104,115,153,154,155,156,157,158,159,160,161,162,],[105,-86,-89,-92,-94,-95,-96,-97,-98,105,-93,-80,-81,-82,-83,-84,-85,-87,-88,-90,-91,]),'NOT_EQ':([64,65,66,68,69,70,71,72,73,104,115,153,154,155,156,157,158,159,160,161,162,],[106,-86,-89,-92,-94,-95,-96,-97,-98,106,-93,-80,-81,-82,-83,-84,-85,-87,-88,-90,-91,]),'LESS_THAN':([64,65,66,68,69,70,71,72,73,104,115,153,154,155,156,157,158,159,160,161,162,],[107,-86,-89,-92,-94,-95,-96,-97,-98,107,-93,-80,-81,-82,-83,-84,-85,-87,-88,-90,-91,]),'GREATER_THAN':([64,65,66,68,69,70,71,72,73,104,115,153,154,155,156,157,158,159,160,161,162,],[108,-86,-89,-92,-94,-95,-96,-97,-98,108,-93,-80,-81,-82,-83,-84,-85,-87,-88,-90,-91,]),'LESS_EQ':([64,65,66,68,69,70,71,72,73,104,115,153,154,155,156,157,158,159,160,161,162,],[109,-86,-89,-92,-94,-95,-96,-97,-98,109,-93,-80,-81,-82,-83,-84,-85,-87,-88,-90,-91,]),'GREATER_EQ':([64,65,66,68,69,70,71,72,73,104,115,153,154,155,156,157,158,159,160,161,162,],[110,-86,-89,-92,-94,-95,-96,-97,-98,110,-93,-80,-81,-82,-83,-84,-85,-87,-88,-90,-91,]),'PLUS':([65,66,68,69,70,71,72,73,115,153,154,155,156,157,158,159,160,161,162,],[111,-89,-92,-94,-95,-96,-97,-98,-93,111,111,111,111,111,111,-87,-88,-90,-91,]),'DIVIDE':([66,68,69,70,71,72,73,115,159,160,161,162,],[114,-92,-94,-95,-96,-97,-98,-93,114,114,-90,-91,]),'INT':([85,172,186,205,212,229,250,],[128,128,128,128,128,128,128,]),'DECIMAL':([85,172,186,205,212,229,250,],[129,129,129,129,129,129,129,]),'BIT':([85,172,186,205,212,229,250,],[130,130,130,130,130,130,130,]),'NCHAR':([85,172,186,205,212,229,250,],[131,131,131,131,131,131,131,]),'NVARCHAR':([85,172,186,205,212,229,250,],[132,132,132,132,132,132,132,]),'DATE':([85,172,186,205,212,229,250,],[133,133,133,133,133,133,133,]),'DATETIME':([85,172,186,205,212,229,250,],[134,134,134,134,134,134,134,]),'ADD':([98,],[146,]),'NOT':([128,129,130,131,132,133,134,200,],[-67,-68,-69,-70,-71,-72,-73,225,]),'NULL':([128,129,130,131,132,133,134,200,225,],[-67,-68,-69,-70,-71,-72,-73,226,248,]),'PRIMARY':([128,129,130,131,132,133,134,200,224,226,248,],[-67,-68,-69,-70,-71,-72,-73,-36,246,-35,-34,]),'REFERENCE':([128,129,130,131,132,133,134,200,224,226,248,],[-67,-68,-69,-70,-71,-72,-73,-36,247,-35,-34,]),'COLUMN':([146,147,],[188,189,]),'RETURN':([203,],[229,]),'VALUES':([211,],[236,]),'KEY':([246,],[259,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'init':([0,],[1,]),'statements':([0,120,251,270,],[2,168,263,276,]),'statement':([2,100,168,191,263,276,],[3,149,3,215,3,3,]),'create_database_statement':([2,100,168,191,263,276,],[4,4,4,4,4,4,]),'use_statement':([2,100,168,191,263,276,],[5,5,5,5,5,5,]),'declare_statement':([2,100,168,191,263,276,],[6,6,6,6,6,6,]),'set_statement':([2,100,168,191,263,276,],[7,7,7,7,7,7,]),'create_table_statement':([2,100,168,191,263,276,],[8,8,8,8,8,8,]),'select_statement':([2,100,168,191,263,276,],[9,9,9,9,9,9,]),'insert_statement':([2,100,168,191,263,276,],[10,10,10,10,10,10,]),'create_function_statement':([2,100,168,191,263,276,],[11,11,11,11,11,11,]),'create_procedure_statement':([2,100,168,191,263,276,],[12,12,12,12,12,12,]),'alter_table_statement':([2,100,168,191,263,276,],[13,13,13,13,13,13,]),'if_statement':([2,100,168,191,263,276,],[14,14,14,14,14,14,]),'exec_statement':([2,100,168,191,263,276,],[15,15,15,15,15,15,]),'drop_table_statement':([2,100,168,191,263,276,],[16,16,16,16,16,16,]),'case_statement':([2,100,168,191,263,276,],[17,17,17,17,17,17,]),'update_statement':([2,100,168,191,263,276,],[18,18,18,18,18,18,]),'while_statement':([2,100,168,191,263,276,],[19,19,19,19,19,19,]),'truncate_statement':([2,100,168,191,263,276,],[20,20,20,20,20,20,]),'delete_statement':([2,100,168,191,263,276,],[21,21,21,21,21,21,]),'assignments':([25,],[43,]),'columns':([26,145,],[45,187,]),'column':([26,90,145,],[47,138,47,]),'call_function_prod':([26,90,145,],[49,49,49,]),'a':([30,34,60,74,75,88,92,93,94,95,96,151,164,165,170,179,181,182,195,196,216,217,245,252,256,257,],[59,77,102,117,118,136,140,141,142,143,144,192,193,194,199,207,208,209,219,220,241,242,258,117,267,268,]),'b':([30,34,60,74,75,88,92,93,94,95,96,101,151,164,165,170,179,181,182,195,196,216,217,245,252,256,257,],[61,61,61,61,61,61,61,61,61,61,61,150,61,61,61,61,61,61,61,61,61,61,61,61,61,61,61,]),'c':([30,34,60,74,75,88,92,93,94,95,96,101,103,151,164,165,170,179,181,182,195,196,216,217,245,252,256,257,],[62,62,62,62,62,62,62,62,62,62,62,62,152,62,62,62,62,62,62,62,62,62,62,62,62,62,62,62,]),'d':([30,34,60,63,74,75,88,92,93,94,95,96,101,103,151,164,165,170,179,181,182,195,196,216,217,245,252,256,257,],[64,64,64,104,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,]),'e':([30,34,60,63,74,75,88,92,93,94,95,96,101,103,105,106,107,108,109,110,151,164,165,170,179,181,182,195,196,216,217,245,252,256,257,],[65,65,65,65,65,65,65,65,65,65,65,65,65,65,153,154,155,156,157,158,65,65,65,65,65,65,65,65,65,65,65,65,65,65,65,]),'f':([30,34,60,63,74,75,88,92,93,94,95,96,101,103,105,106,107,108,109,110,111,112,151,164,165,170,179,181,182,195,196,216,217,245,252,256,257,],[66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,159,160,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,]),'g':([30,34,60,63,74,75,88,92,93,94,95,96,101,103,105,106,107,108,109,110,111,112,113,114,151,164,165,170,179,181,182,195,196,216,217,245,252,256,257,],[68,68,68,68,68,68,68,68,68,68,68,68,68,68,68,68,68,68,68,68,68,68,161,162,68,68,68,68,68,68,68,68,68,68,68,68,68,68,68,]),'h':([30,34,60,63,67,74,75,88,92,93,94,95,96,101,103,105,106,107,108,109,110,111,112,113,114,151,164,165,170,179,181,182,195,196,216,217,245,252,256,257,],[69,69,69,69,115,69,69,69,69,69,69,69,69,69,69,69,69,69,69,69,69,69,69,69,69,69,69,69,69,69,69,69,69,69,69,69,69,69,69,69,]),'vals':([74,252,],[116,264,]),'type':([85,172,186,205,212,229,250,],[127,200,210,231,237,249,262,]),'column_assignments':([119,],[167,]),'properties':([124,],[173,]),'property':([124,202,],[174,228,]),'parameters':([125,126,],[175,177,]),'when_statement':([194,267,],[218,273,]),'null_prod':([200,],[224,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> init","S'",1,None,None,None),
  ('init -> statements','init',1,'p_init','grammar.py',198),
  ('statements -> statements statement','statements',2,'p_statements','grammar.py',202),
  ('statements -> <empty>','statements',0,'p_statements_2','grammar.py',206),
  ('statement -> create_database_statement','statement',1,'p_statement','grammar.py',210),
  ('statement -> use_statement','statement',1,'p_statement','grammar.py',211),
  ('statement -> declare_statement','statement',1,'p_statement','grammar.py',212),
  ('statement -> set_statement','statement',1,'p_statement','grammar.py',213),
  ('statement -> create_table_statement','statement',1,'p_statement','grammar.py',214),
  ('statement -> select_statement','statement',1,'p_statement','grammar.py',215),
  ('statement -> insert_statement','statement',1,'p_statement','grammar.py',216),
  ('statement -> create_function_statement','statement',1,'p_statement','grammar.py',217),
  ('statement -> create_procedure_statement','statement',1,'p_statement','grammar.py',218),
  ('statement -> alter_table_statement','statement',1,'p_statement','grammar.py',219),
  ('statement -> if_statement','statement',1,'p_statement','grammar.py',220),
  ('statement -> exec_statement','statement',1,'p_statement','grammar.py',221),
  ('statement -> drop_table_statement','statement',1,'p_statement','grammar.py',222),
  ('statement -> case_statement','statement',1,'p_statement','grammar.py',223),
  ('statement -> update_statement','statement',1,'p_statement','grammar.py',224),
  ('statement -> while_statement','statement',1,'p_statement','grammar.py',225),
  ('statement -> truncate_statement','statement',1,'p_statement','grammar.py',226),
  ('statement -> delete_statement','statement',1,'p_statement','grammar.py',227),
  ('create_database_statement -> CREATE DATA BASE NAME SEMICOLON','create_database_statement',5,'p_create_database_statement','grammar.py',233),
  ('use_statement -> USE NAME SEMICOLON','use_statement',3,'p_use_statement','grammar.py',238),
  ('declare_statement -> DECLARE ID AS type SEMICOLON','declare_statement',5,'p_declare_statement','grammar.py',243),
  ('set_statement -> SET assignments SEMICOLON','set_statement',3,'p_set_statement','grammar.py',248),
  ('assignments -> assignments COMMA ID ASSIGN a','assignments',5,'p_assignments','grammar.py',253),
  ('assignments -> ID ASSIGN a','assignments',3,'p_assignments_2','grammar.py',257),
  ('create_table_statement -> CREATE TABLE NAME L_PAREN properties R_PAREN SEMICOLON','create_table_statement',7,'p_create_table_statement','grammar.py',262),
  ('properties -> properties COMMA property','properties',3,'p_properties','grammar.py',266),
  ('properties -> property','properties',1,'p_properties_2','grammar.py',269),
  ('property -> NAME type null_prod PRIMARY KEY','property',5,'p_property','grammar.py',273),
  ('property -> NAME type null_prod','property',3,'p_property_2','grammar.py',277),
  ('property -> NAME type null_prod REFERENCE NAME L_PAREN NAME R_PAREN','property',8,'p_property_3','grammar.py',281),
  ('null_prod -> NOT NULL','null_prod',2,'p_null_prod','grammar.py',285),
  ('null_prod -> NULL','null_prod',1,'p_null_prod_2','grammar.py',288),
  ('null_prod -> <empty>','null_prod',0,'p_null_prod_3','grammar.py',292),
  ('select_statement -> SELECT columns FROM NAME SEMICOLON','select_statement',5,'p_select_statement','grammar.py',297),
  ('select_statement -> SELECT columns FROM NAME WHERE a SEMICOLON','select_statement',7,'p_select_statement_2','grammar.py',301),
  ('insert_statement -> INSERT INTO NAME L_PAREN columns R_PAREN VALUES L_PAREN vals R_PAREN SEMICOLON','insert_statement',11,'p_insert_statement','grammar.py',307),
  ('columns -> columns COMMA column','columns',3,'p_columns','grammar.py',313),
  ('columns -> column','columns',1,'p_columns_2','grammar.py',317),
  ('column -> TIMES','column',1,'p_column','grammar.py',321),
  ('column -> NAME','column',1,'p_column','grammar.py',322),
  ('column -> call_function_prod','column',1,'p_column','grammar.py',323),
  ('vals -> vals COMMA a','vals',3,'p_vals','grammar.py',327),
  ('vals -> a','vals',1,'p_vals_2','grammar.py',331),
  ('create_function_statement -> CREATE FUNCTION NAME L_PAREN parameters R_PAREN RETURN type AS BEGIN statements END SEMICOLON','create_function_statement',13,'p_create_function_statement','grammar.py',336),
  ('create_procedure_statement -> CREATE PROCEDURE NAME L_PAREN parameters R_PAREN AS BEGIN statements END SEMICOLON','create_procedure_statement',11,'p_create_procedure_statement','grammar.py',340),
  ('parameters -> parameters COMMA ID AS type','parameters',5,'p_parameters','grammar.py',343),
  ('parameters -> ID AS type','parameters',3,'p_parameters_2','grammar.py',347),
  ('alter_table_statement -> ALTER TABLE NAME ADD COLUMN NAME type SEMICOLON','alter_table_statement',8,'p_alter_table_statement','grammar.py',351),
  ('alter_table_statement -> ALTER TABLE NAME DROP COLUMN NAME SEMICOLON','alter_table_statement',7,'p_alter_table_statement_2','grammar.py',355),
  ('if_statement -> IF a THEN statement END IF SEMICOLON','if_statement',7,'p_if_statement','grammar.py',368),
  ('if_statement -> IF a THEN statement ELSE statement END IF SEMICOLON','if_statement',9,'p_if_statement2','grammar.py',371),
  ('if_statement -> IF L_PAREN a COMMA a COMMA a R_PAREN SEMICOLON','if_statement',9,'p_if_statement3','grammar.py',375),
  ('exec_statement -> EXEC NAME vals SEMICOLON','exec_statement',4,'p_exec_statement','grammar.py',381),
  ('drop_table_statement -> DROP TABLE NAME SEMICOLON','drop_table_statement',4,'p_drop_table_statement','grammar.py',386),
  ('update_statement -> UPDATE NAME SET column_assignments WHERE a SEMICOLON','update_statement',7,'p_update_statement','grammar.py',391),
  ('column_assignments -> column_assignments COMMA NAME ASSIGN a','column_assignments',5,'p_column_assignments','grammar.py',395),
  ('column_assignments -> NAME ASSIGN a','column_assignments',3,'p_column_assignments_2','grammar.py',399),
  ('while_statement -> WHILE a BEGIN statements END SEMICOLON','while_statement',6,'p_while_statement','grammar.py',405),
  ('truncate_statement -> TRUNCATE TABLE NAME SEMICOLON','truncate_statement',4,'p_truncate_statement','grammar.py',411),
  ('delete_statement -> DELETE FROM NAME WHERE a SEMICOLON','delete_statement',6,'p_delete_statement','grammar.py',416),
  ('case_statement -> CASE WHEN a THEN a when_statement ELSE THEN a END','case_statement',10,'p_case_statement','grammar.py',421),
  ('when_statement -> WHEN a THEN a when_statement','when_statement',5,'p_when_statement','grammar.py',424),
  ('when_statement -> <empty>','when_statement',0,'p_when_statement2','grammar.py',427),
  ('type -> INT','type',1,'p_type','grammar.py',430),
  ('type -> DECIMAL','type',1,'p_type','grammar.py',431),
  ('type -> BIT','type',1,'p_type','grammar.py',432),
  ('type -> NCHAR','type',1,'p_type','grammar.py',433),
  ('type -> NVARCHAR','type',1,'p_type','grammar.py',434),
  ('type -> DATE','type',1,'p_type','grammar.py',435),
  ('type -> DATETIME','type',1,'p_type','grammar.py',436),
  ('a -> a OR b','a',3,'p_a','grammar.py',439),
  ('a -> b','a',1,'p_a_2','grammar.py',442),
  ('b -> b AND c','b',3,'p_b','grammar.py',445),
  ('b -> c','b',1,'p_b_2','grammar.py',449),
  ('c -> NOT_SIGN d','c',2,'p_c','grammar.py',453),
  ('c -> d','c',1,'p_c_2','grammar.py',457),
  ('d -> d EQUALS e','d',3,'p_d','grammar.py',461),
  ('d -> d NOT_EQ e','d',3,'p_d','grammar.py',462),
  ('d -> d LESS_THAN e','d',3,'p_d','grammar.py',463),
  ('d -> d GREATER_THAN e','d',3,'p_d','grammar.py',464),
  ('d -> d LESS_EQ e','d',3,'p_d','grammar.py',465),
  ('d -> d GREATER_EQ e','d',3,'p_d','grammar.py',466),
  ('d -> e','d',1,'p_d_2','grammar.py',471),
  ('e -> e PLUS f','e',3,'p_e','grammar.py',475),
  ('e -> e MINUS f','e',3,'p_e','grammar.py',476),
  ('e -> f','e',1,'p_e_2','grammar.py',480),
  ('f -> f TIMES g','f',3,'p_f','grammar.py',484),
  ('f -> f DIVIDE g','f',3,'p_f','grammar.py',485),
  ('f -> g','f',1,'p_f_2','grammar.py',489),
  ('g -> MINUS h','g',2,'p_g','grammar.py',493),
  ('g -> h','g',1,'p_g_2','grammar.py',497),
  ('h -> INTEGER_VALUE','h',1,'p_h','grammar.py',501),
  ('h -> DECIMAL_VALUE','h',1,'p_h','grammar.py',502),
  ('h -> STRING','h',1,'p_h','grammar.py',503),
  ('h -> ID','h',1,'p_h','grammar.py',504),
  ('call_function_prod -> HOY L_PAREN R_PAREN','call_function_prod',3,'p_call_function_prod','grammar.py',508),
  ('call_function_prod -> CONCATENAR L_PAREN a COMMA a R_PAREN','call_function_prod',6,'p_call_function_prod','grammar.py',509),
  ('call_function_prod -> SUBSTRAER L_PAREN a R_PAREN','call_function_prod',4,'p_call_function_prod','grammar.py',510),
  ('call_function_prod -> CONTAR L_PAREN a R_PAREN','call_function_prod',4,'p_call_function_prod','grammar.py',511),
  ('call_function_prod -> SUMA L_PAREN a R_PAREN','call_function_prod',4,'p_call_function_prod','grammar.py',512),
  ('call_function_prod -> CAS L_PAREN a AS type R_PAREN','call_function_prod',6,'p_call_function_prod','grammar.py',513),
]
