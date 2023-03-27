import re
import ply.lex as lex

texto = 'Era uma vez, um gato maltês.'

tokens = [
    'PALAVRA',
    'VIRGULA',
    'OUTROS'
]

t_PALAVRA = r'\w+'
t_VIRGULA = r','
t_OUTROS = r'[.!"]'

t_ignore = ' \t\n'

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