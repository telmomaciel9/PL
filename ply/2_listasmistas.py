import re
import ply.lex as lex

texto = '[ 1,5, palavra, False ,3.14,   0, fim]'

tokens = [
    'PALAVRA',
    'BOOL',
    'INT',
    'FLOAT'
]

literals = '[],'

#t_BOOL = r'True|False'
#t_INT = r'\d+'
#t_FLOAT = r'\d+\.\d+'
#t_PALAVRA = r'\w+'

t_ignore = ' \t\n'

def t_INT(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_FLOAT(t):
    r'\d+\.\d+'
    t.value = float(t.value)
    return t

def t_PALAVRA(t):
    r'[a-zA-Z]\w*'
    if t.value in ['True','False']:
        t.type = 'BOOL'
    return t

def t_error(t):
    print(f"Carácter ilegal {t.value[0]}")
    t.lexer.skip(1)


lexer = lex.lex()

lexer.input(texto)


#for tok in lexer: 
#    print(tok)

#while True:
#    tok = lexer.token()
#    if not tok:
#        break
#    print(tok)

while t:=lexer.token():
    print(t)