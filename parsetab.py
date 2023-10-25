
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'ID IGNORE LBRACE RBRACE SEMICOLON STRUCT TYPE TYPEDEF\n    declaration : STRUCT ID LBRACE fields RBRACE SEMICOLON  \n             \n    \n    fields : TYPE ID SEMICOLON fields\n           | TYPE ID SEMICOLON\n    '
    
_lr_action_items = {'STRUCT':([0,],[2,]),'$end':([1,9,],[0,-1,]),'ID':([2,6,],[3,8,]),'LBRACE':([3,],[4,]),'TYPE':([4,10,],[6,6,]),'RBRACE':([5,10,11,],[7,-3,-2,]),'SEMICOLON':([7,8,],[9,10,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'declaration':([0,],[1,]),'fields':([4,10,],[5,11,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> declaration","S'",1,None,None,None),
  ('declaration -> STRUCT ID LBRACE fields RBRACE SEMICOLON','declaration',6,'p_declaration','structuredecleration.py',58),
  ('fields -> TYPE ID SEMICOLON fields','fields',4,'p_fields','structuredecleration.py',65),
  ('fields -> TYPE ID SEMICOLON','fields',3,'p_fields','structuredecleration.py',66),
]
