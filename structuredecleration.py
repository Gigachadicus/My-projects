import ply.lex as lex
import ply.yacc as yacc

tokens = (
    'TYPEDEF',
    'STRUCT',
    'TYPE',
    'ID',
    'SEMICOLON',
    'LBRACE',
    'RBRACE',
    'IGNORE'
)

t_IGNORE = r' \t'

def t_TYPEDEF(t):
    r'typedef'
    return t

def t_STRUCT(t):
    r'struct'
    return t

def t_TYPE(t):
    r'int|char|float|double'
    return t

def t_ID(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    return t

def t_INTEGER(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_SEMICOLON(t):
    r';'
    return t

def t_LBRACE(t):
    r'\{'
    return t

def t_RBRACE(t):
    r'\}'
    return t

def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

lexer = lex.lex()

def p_declaration(p):
    '''
    declaration : STRUCT ID LBRACE fields RBRACE SEMICOLON  
             
    '''
    print("Valid structure declaration")

def p_fields(p):
    '''
    fields : TYPE ID SEMICOLON fields
           | TYPE ID SEMICOLON
    '''

def p_error(p):
    print("Syntax error in input!")

parser = yacc.yacc()

# Test the lexer with example input
input_text = "struct ants{int from; int to;};"
lexer.input(input_text)

# Print the tokens recognized by the lexer
for token in lexer:
    print(f"Token Type: {token.type}, Value: {token.value}")

s = "struct ants{int from; int to;};"
parser.parse(s)
