import ply.lex as lex

reserved = {'car': 'CAR', 'cdr': 'CDR', 'cons': 'CONS', 'if': 'IF', 'and': 'AND', 'or': 'OR'}

tokens = ['NUMBER', 'BOOL', 'ID', 'LPAR', 'RPAR', 'SEMI', 'PLUS', 'MINUS', 'MULT', 'DIV', 'LESS', 'GREAT', 'LIST'] + \
         list(reserved.values())

t_LPAR = r'\('
t_RPAR = r'\)'
t_SEMI = r';'
t_PLUS = r'\+'
t_MINUS = r'-'
t_MULT = r'\*'
t_DIV = r'/'
t_LESS = r'\<'
t_GREAT = r'\>'
t_IF = r'[iI][fF]'
t_OR = r'[oO][rR]'
t_AND = r'[aA][nN][dD]'

# Ignored characters
t_ignore = " \r\n\t"
t_ignore_COMMENT = r'\#.*'


def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    # t.lexer.skip(1)
    raise Exception('LEXER ERROR')


def t_LIST(t):
    r'\w*([-+]?[0-9]+(\.([0-9]+)?)?\w*)+'
    t.type = 'LIST'
    str1 = str(t.value)
    str1.replace('(', '')
    str1.replace(')', '')
    arr = str1.split(' ')
    t.value = arr
    print(t.value)
    return t


def t_NUMBER(t):
    r'[-+]?[0-9]+(\.([0-9]+)?)?'
    t.value = float(t.value)
    t.type = 'NUMBER'
    return t


def t_BOOL(t):
    r'([Tt][Rr][Uu][Ee]|[Ff][Aa][Ll][Ss][Ee])'
    t.type = 'BOOL'
    if str(t.value).lower() == 'true':
        t.value = True
    elif str(t.value).lower() == 'false':
        t.value = False
    return t


def t_ID(t):
    r'[a-zA-Z][_a-zA-Z0-9]*'
    t.type = reserved.get(t.value.lower(), 'ID')
    return t


lexer = lex.lex()
