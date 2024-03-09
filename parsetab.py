
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'leftPLUSMINUSleftTIMESDIVIDEnonassocLTLTEGTGTENErightUMINUSASSIGN CALL COMMA COMMENT DIVIDE DO DOT FOR FUNCTION GT GTE ID IF LBRACE LPARENT LT LTE MINUS NE NUMBER PLUS PRINT RBRACE READ RETURN RPARENT SEMICOLON STRING TIMES VAR WHILEprogram : program statement\n               | statementstatement : expression SEMICOLONstatement : VAR ID ASSIGN expression SEMICOLON\n                 | ID ASSIGN expression SEMICOLONstatement : FUNCTION ID LPARENT RPARENT block\n                 | FUNCTION ID LPARENT VAR ID RPARENT blockstatement : IF LPARENT expression RPARENT blockstatement : WHILE LPARENT expression RPARENT blockstatement : FOR LPARENT statement SEMICOLON expression SEMICOLON expression RPARENT blockstatement : RETURN expression SEMICOLONblock : LBRACE statements RBRACE\n             | LBRACE RBRACEstatements : statements statement\n                  | statementexpression : expression PLUS expression\n                  | expression MINUS expression\n                  | expression TIMES expression\n                  | expression DIVIDE expressionexpression : MINUS expression %prec UMINUSexpression : LPARENT expression RPARENTexpression : NUMBERexpression : IDexpression : expression LT expression\n                  | expression LTE expression\n                  | expression GT expression\n                  | expression GTE expression\n                  | expression NE expressionexpression : STRINGstatement : PRINT LPARENT expression RPARENT SEMICOLONstatement : CALL ID LPARENT arguments RPARENT SEMICOLONarguments : arguments COMMA expression\n                 | expression\n                 | emptyempty :'
    
_lr_action_items = {'VAR':([0,1,2,17,18,35,51,56,60,70,71,72,74,75,77,80,81,82,85,87,88,89,92,],[4,4,-2,-1,-3,4,62,-11,-5,-4,-6,4,-8,-9,-30,4,-13,-15,-31,-12,-14,-7,-10,]),'ID':([0,1,2,4,6,7,11,13,14,17,18,19,20,21,22,23,24,25,26,27,29,33,34,35,37,49,56,58,60,62,65,70,71,72,74,75,77,79,80,81,82,84,85,87,88,89,92,],[5,5,-2,28,30,32,32,38,32,-1,-3,32,32,32,32,32,32,32,32,32,32,32,32,5,32,32,-11,32,-5,73,32,-4,-6,5,-8,-9,-30,32,5,-13,-15,32,-31,-12,-14,-7,-10,]),'FUNCTION':([0,1,2,17,18,35,56,60,70,71,72,74,75,77,80,81,82,85,87,88,89,92,],[6,6,-2,-1,-3,6,-11,-5,-4,-6,6,-8,-9,-30,6,-13,-15,-31,-12,-14,-7,-10,]),'IF':([0,1,2,17,18,35,56,60,70,71,72,74,75,77,80,81,82,85,87,88,89,92,],[8,8,-2,-1,-3,8,-11,-5,-4,-6,8,-8,-9,-30,8,-13,-15,-31,-12,-14,-7,-10,]),'WHILE':([0,1,2,17,18,35,56,60,70,71,72,74,75,77,80,81,82,85,87,88,89,92,],[9,9,-2,-1,-3,9,-11,-5,-4,-6,9,-8,-9,-30,9,-13,-15,-31,-12,-14,-7,-10,]),'FOR':([0,1,2,17,18,35,56,60,70,71,72,74,75,77,80,81,82,85,87,88,89,92,],[10,10,-2,-1,-3,10,-11,-5,-4,-6,10,-8,-9,-30,10,-13,-15,-31,-12,-14,-7,-10,]),'RETURN':([0,1,2,17,18,35,56,60,70,71,72,74,75,77,80,81,82,85,87,88,89,92,],[11,11,-2,-1,-3,11,-11,-5,-4,-6,11,-8,-9,-30,11,-13,-15,-31,-12,-14,-7,-10,]),'PRINT':([0,1,2,17,18,35,56,60,70,71,72,74,75,77,80,81,82,85,87,88,89,92,],[12,12,-2,-1,-3,12,-11,-5,-4,-6,12,-8,-9,-30,12,-13,-15,-31,-12,-14,-7,-10,]),'CALL':([0,1,2,17,18,35,56,60,70,71,72,74,75,77,80,81,82,85,87,88,89,92,],[13,13,-2,-1,-3,13,-11,-5,-4,-6,13,-8,-9,-30,13,-13,-15,-31,-12,-14,-7,-10,]),'MINUS':([0,1,2,3,5,7,11,14,15,16,17,18,19,20,21,22,23,24,25,26,27,29,31,32,33,34,35,36,37,39,40,41,42,43,44,45,46,47,48,49,50,52,53,54,56,57,58,59,60,65,68,70,71,72,74,75,76,77,79,80,81,82,84,85,86,87,88,89,90,92,],[14,14,-2,20,-23,14,14,14,-22,-29,-1,-3,14,14,14,14,14,14,14,14,14,14,20,-23,14,14,14,20,14,-20,-16,-17,-18,-19,-24,-25,-26,-27,-28,14,20,-21,20,20,-11,20,14,20,-5,14,20,-4,-6,14,-8,-9,20,-30,14,14,-13,-15,14,-31,20,-12,-14,-7,20,-10,]),'LPARENT':([0,1,2,7,8,9,10,11,12,14,17,18,19,20,21,22,23,24,25,26,27,29,30,33,34,35,37,38,49,56,58,60,65,70,71,72,74,75,77,79,80,81,82,84,85,87,88,89,92,],[7,7,-2,7,33,34,35,7,37,7,-1,-3,7,7,7,7,7,7,7,7,7,7,51,7,7,7,7,58,7,-11,7,-5,7,-4,-6,7,-8,-9,-30,7,7,-13,-15,7,-31,-12,-14,-7,-10,]),'NUMBER':([0,1,2,7,11,14,17,18,19,20,21,22,23,24,25,26,27,29,33,34,35,37,49,56,58,60,65,70,71,72,74,75,77,79,80,81,82,84,85,87,88,89,92,],[15,15,-2,15,15,15,-1,-3,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,-11,15,-5,15,-4,-6,15,-8,-9,-30,15,15,-13,-15,15,-31,-12,-14,-7,-10,]),'STRING':([0,1,2,7,11,14,17,18,19,20,21,22,23,24,25,26,27,29,33,34,35,37,49,56,58,60,65,70,71,72,74,75,77,79,80,81,82,84,85,87,88,89,92,],[16,16,-2,16,16,16,-1,-3,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,-11,16,-5,16,-4,-6,16,-8,-9,-30,16,16,-13,-15,16,-31,-12,-14,-7,-10,]),'$end':([1,2,17,18,56,60,70,71,74,75,77,81,85,87,89,92,],[0,-2,-1,-3,-11,-5,-4,-6,-8,-9,-30,-13,-31,-12,-7,-10,]),'SEMICOLON':([3,5,15,16,18,32,36,39,40,41,42,43,44,45,46,47,48,50,52,55,56,59,60,66,70,71,74,75,76,77,78,81,85,87,89,92,],[18,-23,-22,-29,-3,-23,56,-20,-16,-17,-18,-19,-24,-25,-26,-27,-28,60,-21,65,-11,70,-5,77,-4,-6,-8,-9,84,-30,85,-13,-31,-12,-7,-10,]),'PLUS':([3,5,15,16,31,32,36,39,40,41,42,43,44,45,46,47,48,50,52,53,54,57,59,68,76,86,90,],[19,-23,-22,-29,19,-23,19,-20,-16,-17,-18,-19,-24,-25,-26,-27,-28,19,-21,19,19,19,19,19,19,19,19,]),'TIMES':([3,5,15,16,31,32,36,39,40,41,42,43,44,45,46,47,48,50,52,53,54,57,59,68,76,86,90,],[21,-23,-22,-29,21,-23,21,-20,21,21,-18,-19,-24,-25,-26,-27,-28,21,-21,21,21,21,21,21,21,21,21,]),'DIVIDE':([3,5,15,16,31,32,36,39,40,41,42,43,44,45,46,47,48,50,52,53,54,57,59,68,76,86,90,],[22,-23,-22,-29,22,-23,22,-20,22,22,-18,-19,-24,-25,-26,-27,-28,22,-21,22,22,22,22,22,22,22,22,]),'LT':([3,5,15,16,31,32,36,39,40,41,42,43,44,45,46,47,48,50,52,53,54,57,59,68,76,86,90,],[23,-23,-22,-29,23,-23,23,-20,23,23,23,23,None,None,None,None,None,23,-21,23,23,23,23,23,23,23,23,]),'LTE':([3,5,15,16,31,32,36,39,40,41,42,43,44,45,46,47,48,50,52,53,54,57,59,68,76,86,90,],[24,-23,-22,-29,24,-23,24,-20,24,24,24,24,None,None,None,None,None,24,-21,24,24,24,24,24,24,24,24,]),'GT':([3,5,15,16,31,32,36,39,40,41,42,43,44,45,46,47,48,50,52,53,54,57,59,68,76,86,90,],[25,-23,-22,-29,25,-23,25,-20,25,25,25,25,None,None,None,None,None,25,-21,25,25,25,25,25,25,25,25,]),'GTE':([3,5,15,16,31,32,36,39,40,41,42,43,44,45,46,47,48,50,52,53,54,57,59,68,76,86,90,],[26,-23,-22,-29,26,-23,26,-20,26,26,26,26,None,None,None,None,None,26,-21,26,26,26,26,26,26,26,26,]),'NE':([3,5,15,16,31,32,36,39,40,41,42,43,44,45,46,47,48,50,52,53,54,57,59,68,76,86,90,],[27,-23,-22,-29,27,-23,27,-20,27,27,27,27,None,None,None,None,None,27,-21,27,27,27,27,27,27,27,27,]),'ASSIGN':([5,28,],[29,49,]),'RPARENT':([15,16,31,32,39,40,41,42,43,44,45,46,47,48,51,52,53,54,57,58,67,68,69,73,86,90,],[-22,-29,52,-23,-20,-16,-17,-18,-19,-24,-25,-26,-27,-28,61,-21,63,64,66,-35,78,-33,-34,83,-32,91,]),'COMMA':([15,16,32,39,40,41,42,43,44,45,46,47,48,52,58,67,68,69,86,],[-22,-29,-23,-20,-16,-17,-18,-19,-24,-25,-26,-27,-28,-21,-35,79,-33,-34,-32,]),'RBRACE':([18,56,60,70,71,72,74,75,77,80,81,82,85,87,88,89,92,],[-3,-11,-5,-4,-6,81,-8,-9,-30,87,-13,-15,-31,-12,-14,-7,-10,]),'LBRACE':([61,63,64,83,91,],[72,72,72,72,72,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'program':([0,],[1,]),'statement':([0,1,35,72,80,],[2,17,55,82,88,]),'expression':([0,1,7,11,14,19,20,21,22,23,24,25,26,27,29,33,34,35,37,49,58,65,72,79,80,84,],[3,3,31,36,39,40,41,42,43,44,45,46,47,48,50,53,54,3,57,59,68,76,3,86,3,90,]),'arguments':([58,],[67,]),'empty':([58,],[69,]),'block':([61,63,64,83,91,],[71,74,75,89,92,]),'statements':([72,],[80,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> program","S'",1,None,None,None),
  ('program -> program statement','program',2,'p_program','sintactico.py',17),
  ('program -> statement','program',1,'p_program','sintactico.py',18),
  ('statement -> expression SEMICOLON','statement',2,'p_statement_expr','sintactico.py',25),
  ('statement -> VAR ID ASSIGN expression SEMICOLON','statement',5,'p_statement_assign','sintactico.py',29),
  ('statement -> ID ASSIGN expression SEMICOLON','statement',4,'p_statement_assign','sintactico.py',30),
  ('statement -> FUNCTION ID LPARENT RPARENT block','statement',5,'p_statement_function','sintactico.py',37),
  ('statement -> FUNCTION ID LPARENT VAR ID RPARENT block','statement',7,'p_statement_function','sintactico.py',38),
  ('statement -> IF LPARENT expression RPARENT block','statement',5,'p_statement_if','sintactico.py',45),
  ('statement -> WHILE LPARENT expression RPARENT block','statement',5,'p_statement_while','sintactico.py',49),
  ('statement -> FOR LPARENT statement SEMICOLON expression SEMICOLON expression RPARENT block','statement',9,'p_statement_for','sintactico.py',53),
  ('statement -> RETURN expression SEMICOLON','statement',3,'p_statement_return','sintactico.py',57),
  ('block -> LBRACE statements RBRACE','block',3,'p_block','sintactico.py',61),
  ('block -> LBRACE RBRACE','block',2,'p_block','sintactico.py',62),
  ('statements -> statements statement','statements',2,'p_statements','sintactico.py',69),
  ('statements -> statement','statements',1,'p_statements','sintactico.py',70),
  ('expression -> expression PLUS expression','expression',3,'p_expression_binop','sintactico.py',77),
  ('expression -> expression MINUS expression','expression',3,'p_expression_binop','sintactico.py',78),
  ('expression -> expression TIMES expression','expression',3,'p_expression_binop','sintactico.py',79),
  ('expression -> expression DIVIDE expression','expression',3,'p_expression_binop','sintactico.py',80),
  ('expression -> MINUS expression','expression',2,'p_expression_uminus','sintactico.py',84),
  ('expression -> LPARENT expression RPARENT','expression',3,'p_expression_group','sintactico.py',88),
  ('expression -> NUMBER','expression',1,'p_expression_number','sintactico.py',92),
  ('expression -> ID','expression',1,'p_expression_name','sintactico.py',96),
  ('expression -> expression LT expression','expression',3,'p_expression_comparison','sintactico.py',100),
  ('expression -> expression LTE expression','expression',3,'p_expression_comparison','sintactico.py',101),
  ('expression -> expression GT expression','expression',3,'p_expression_comparison','sintactico.py',102),
  ('expression -> expression GTE expression','expression',3,'p_expression_comparison','sintactico.py',103),
  ('expression -> expression NE expression','expression',3,'p_expression_comparison','sintactico.py',104),
  ('expression -> STRING','expression',1,'p_expression_string','sintactico.py',108),
  ('statement -> PRINT LPARENT expression RPARENT SEMICOLON','statement',5,'p_statement_print','sintactico.py',112),
  ('statement -> CALL ID LPARENT arguments RPARENT SEMICOLON','statement',6,'p_statement_summon','sintactico.py',116),
  ('arguments -> arguments COMMA expression','arguments',3,'p_arguments','sintactico.py',120),
  ('arguments -> expression','arguments',1,'p_arguments','sintactico.py',121),
  ('arguments -> empty','arguments',1,'p_arguments','sintactico.py',122),
  ('empty -> <empty>','empty',0,'p_empty','sintactico.py',132),
]