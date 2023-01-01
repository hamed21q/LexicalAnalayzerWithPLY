import lex as lex
tokens = [ 'AND',
          'ASSIGNMENT',
          'BINARY',
          'COMMA',
          'LINECOMMENT',
          'MULTILINECOMMENT',
          'RIGHTSQRBRACKET',
          'LEFTSQRBRACKET',
          'DIVISION',
          'NOTEQUAL',
          'CONCAT',
          'EQUAL',
          'NOT',
          'HEXADEC',
          'IDEN',
          'RIGHTBRACE',
          'LEFTBRACE',
          'GREATEREQUAL',
          'GREATER',
          'LESSEQUAL',
          'LESS',
          'SUBSTRACTION',
          'UMINUS',
          'MULTIPLICATION',
          'NUMBER',
          'CIENTIFIC',
          'FLOAT',
          'OR',
          'RIGHTPARENT',
          'LEFTPARENT',
          'MODULO',
          'DOT',
          'SEMICOLON',
          'ADDITION']
reserved = {
    'boolean':'BOOLEAN',
    'break' : 'BREAK',
    'class' : 'CLASS',
    'continue' : 'CONTINUE',
    'else' : 'ELSE',
    'extends' : 'EXTENDS',
    'false' : 'FALSE',
    'if' : 'IF',
    'int' : 'INT',
    'length' : 'LENGTH',
    'new' : 'NEW',
    'null' : 'NULL',
    'return' : 'RETURN',
    'string' : 'STRING',
    'this' : 'THIS',
    'true' : 'TRUE',
    'void' : 'VOID',
    'while' : 'WHILE'
}
tokens += reserved.values()

t_AND = r'(\&\&|AND)'
t_ASSIGNMENT = r'='
t_COMMA = r','
t_LEFTSQRBRACKET = r'\['
t_RIGHTSQRBRACKET = r'\]'
t_DIVISION = r'\/'
t_NOTEQUAL = r'!='
t_EQUAL = r'=='
t_NOT = r'!'
t_LEFTBRACE  = r'\{'
t_RIGHTBRACE = r'\}'
t_GREATEREQUAL = r'>='
t_GREATER = r'>'
t_LESSEQUAL = r'<='
t_LESS = r'<'
t_SUBSTRACTION = r'\-'
t_UMINUS = r'\-'
t_CONCAT = r'\+'
t_MULTIPLICATION = r'\*'
t_OR = r'(\|\|)|(OR)'
t_LEFTPARENT = r'\('
t_RIGHTPARENT = r'\)'
t_MODULO = r'%'
t_DOT = r'\.'
t_SEMICOLON = r';'
t_ADDITION = '\+'

def t_IDEN(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    if t.value in reserved:
        t.type = reserved[ t.value ]
    return t
    
def t_NUMBER(t):
    r'(-)?(\d+)'
    try:
        t.value = int(t.value)
    except ValueError:
        print("ERROR CONVERSION NUMERO %d", t.value)
        t.value = 0
    return t


def t_error(t):
    print ('Illegal character')
    t.lexer.skip(1)

data = input()
lexer = lex.lex()
lexer.input(data)
while True:
    tok = lex.token()
    if not tok:
        break
    print (tok)