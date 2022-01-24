import ply.yacc as yacc
from LISPLexer import tokens


def p_lispStart(p):
    'lispStart : lisp SEMI'
    p[0] = p[1]


def p_lisp_1(p):
    'lisp : NUMBER'
    p[0] = ['num', p[1]]


def p_lisp_2(p):
    'lisp : BOOL'
    p[0] = ['bool', bool(p[1])]


def p_lisp_3(p):
    'lisp : ID'
    p[0] = ['id', p[1]]


def p_lisp_4(p):
    'lisp : LPAR PLUS lisp lisp RPAR'
    p[0] = ['+', p[3], p[4]]


def p_lisp_5(p):
    'lisp : LPAR MINUS lisp lisp RPAR'
    p[0] = ['-', p[3], p[4]]


def p_lisp_6(p):
    'lisp : LPAR MULT lisp lisp RPAR'
    p[0] = ['*', p[3], p[4]]


def p_lisp_7(p):
    'lisp : LPAR DIV lisp lisp RPAR'
    p[0] = ['/', p[3], p[4]]


def p_wae_8(p):
    'lisp : LPAR IF lisp lisp lisp RPAR'
    p[0] = ['if', p[3], p[4], p[5]]


def p_lisp_9(p):
    'lisp : LPAR LESS lisp lisp RPAR'
    p[0] = ['<', p[3], p[4]]


def p_lisp_10(p):
    'lisp : LPAR OR lisp lisp RPAR'
    p[0] = ['or', p[3], p[4]]

def p_lisp_11(p):
    'lisp : LPAR AND lisp lisp RPAR'
    p[0] = ['and', p[3], p[4]]

def p_lisp_12(p):
    'lisp : LPAR GREAT lisp lisp RPAR'
    p[0] = ['>', p[3], p[4]]


def p_alist_1(p):
    'alist : LPAR NUM RPAR'
    p[0] = ['list' , p[2]]


def p_error(p):
    print("Syntax error in input!")


parser = yacc.yacc()
