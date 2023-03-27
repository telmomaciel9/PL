import re
import ply.lex as lex

texto = '''
# This is a heading
## This is a subheading
This is some **bold** text.
This is some *italic* text.
- This is a bullet point
- This is another bullet point
1. This is a numbered list
2. This is another numbered list item
'''

tokens = [
    'TITULO',
    'SUBTITULO',
    'OUTROS',
    'BOLD',
    'ITALIC',
    'BULLETPOINT',
    'NUMBEREDLIST'
]

def t_BOLD(t):
    r'\*\*.+?\*\*'
    print(f'<b> {t.value.strip("* ")} </b>', end='')

def t_ITALIC(t):
    r'\*.+?\*'
    print(f'<i> {t.value.strip("* ")} </i>', end='')

def t_TITULO(t):
    r'\#\s .+'
    print(f'<h1> {t.value.strip("# ")} </h1>', end='')

def t_SUBTITULO(t):
    r'\#\#\s .+'
    print(f'<h2> {t.value.strip("# ")} </h2>', end='')

def t_BULLETPOINT(t):
    r'\-\s .+'
    print(f'<ul> {t.value.strip("- ")} </ul>', end='')

def t_NUMBEREDLIST(t):
    r'\d+\.\s .+'
    print(f'<ol> {t.value.strip(" ")} </ol>', end='')

def t_OUTROS(t):
    r'.|\n'
    print(t.value, end='')

def t_error(t):
    print(f"Carácter ilegal {t.value[0]}")
    t.lexer.skip(1)


lexer = lex.lex()

lexer.input(texto)

while t:=lexer.token():
    print(t)