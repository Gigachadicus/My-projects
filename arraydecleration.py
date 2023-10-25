import ply.lex as lex
import ply.yacc as yacc

tokens = (
    'TYPE',
    'ID',
    'INTEGER',
    'SEMICOLON',
    'LBRACE',
    'RBRACE',
    'LBRACKET',
    'RBRACKET',
    'COMMA',
    'EQUAL'
)

t_EQUAL = r'='

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

def t_LBRACKET(t):
    r'\['
    return t

def t_RBRACKET(t):
    r'\]'
    return t

def t_SEMICOLON(t):
    r';'
    return t

def t_COMMA(t):
    r','
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
    declaration : TYPE ID DIMENSION SEMICOLON  
             | TYPE ID DIMENSION EQUAL LBRACE NUMBERS RBRACE SEMICOLON
    '''
    print("Valid array declaration")

def p_NUMBERS(p):
    '''
    NUMBERS : INTEGER
             | NUMBERS COMMA INTEGER
    '''

def p_DIMENSION(p):
    '''
    DIMENSION : DIMENSION LBRACKET INTEGER RBRACKET
             | LBRACKET INTEGER RBRACKET
    '''

def p_error(p):
    print("Syntax error in input!")

parser = yacc.yacc()
lexer = lex.lex()

# Test the lexer with example input
input_text = "int x[3][5];"
lexer.input(input_text)

# Print the tokens recognized by the lexer
for token in lexer:
    print(f"Token Type: {token.type}, Value: {token.value}")

s = "int ARR[3]={1,2,3};"
parser.parse(s)

