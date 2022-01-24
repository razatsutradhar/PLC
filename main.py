import ply.lex as lex
from LISPParser import parser

def eval_expression(tree):
  if tree[0] == 'num':
    return tree[1]
  elif tree[0] == 'id':
    return 'ERROR: Cannot evaluate ID '+tree[1]
  elif tree[0] == '+' or tree[0] == '-' or tree[0] == '*' or tree[0] == '/':
    v1 = eval_expression(tree[1])
    if isinstance(v1,str):
      return v1
    v2 = eval_expression(tree[2])
    if isinstance(v2,str):
      return v2
    if tree[0] == '+':
      return v1+v2
    elif tree[0] == '-':
      return v1-v2
    elif tree[0] == '*':
      return v1*v2
    elif v2 != 0:
      return v1/v2
    else:
      return 'ERROR: Divide by Zero'
  elif tree[0] == 'if':
    v1 = eval_expression(tree[1])
    if isinstance(v1,str):
      return v1
    if v1 != 0:
      return eval_expression(tree[2])
    else:
      return eval_expression(tree[3])
  else: #with clause
    return "WITH not implemented!"