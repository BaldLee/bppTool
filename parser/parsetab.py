
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'AA ACT AF AND COMMA EA EG GE LBRACE LBRACK LPAREN MINUS NOT NUMBER OR PLUS RBRACE RBRACK RPAREN SEMICOLON VARtest : atomvariables : VARvariables : variables COMMA VARrules : rulerules : rules rulerule : LBRACK VAR COMMA ACT COMMA LPAREN variables RPAREN RBRACKatom : plusexpes GE NUMBERplusexpes : VARplusexpes : plusexpes PLUS VAR'
    
_lr_action_items = {'VAR':([0,6,],[4,8,]),'$end':([1,2,7,],[0,-1,-7,]),'GE':([3,4,8,],[5,-8,-9,]),'PLUS':([3,4,8,],[6,-8,-9,]),'NUMBER':([5,],[7,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'test':([0,],[1,]),'atom':([0,],[2,]),'plusexpes':([0,],[3,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> test","S'",1,None,None,None),
  ('test -> atom','test',1,'p_test','parser.py',133),
  ('variables -> VAR','variables',1,'p_variables_var','parser.py',138),
  ('variables -> variables COMMA VAR','variables',3,'p_variables_combine','parser.py',144),
  ('rules -> rule','rules',1,'p_rules_rule','parser.py',150),
  ('rules -> rules rule','rules',2,'p_rules_combine','parser.py',156),
  ('rule -> LBRACK VAR COMMA ACT COMMA LPAREN variables RPAREN RBRACK','rule',9,'p_rule','parser.py',162),
  ('atom -> plusexpes GE NUMBER','atom',3,'p_atom','parser.py',167),
  ('plusexpes -> VAR','plusexpes',1,'p_pulsexpes_var','parser.py',172),
  ('plusexpes -> plusexpes PLUS VAR','plusexpes',3,'p_plusexpes_combine','parser.py',177),
]