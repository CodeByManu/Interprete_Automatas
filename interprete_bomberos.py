import ply.lex as lex
import ply.yacc as yacc
import os

# palabra_reservada: TOKEN
reserved = {
    'salir': 'EXIT',
}

""" 
'10-0-1': 'FB',  # Fuego Base (piso bajo)
'10-0-2': 'FA',  # Fuego en Altura (piso alto)
'10-4-1': 'CC',  # Choque Chico
'10-4-2': 'CG',  # Choque Grave
"""

# Lista de tokens
tokens = [
    'CODE',
    'KW'
    ]+ list(reserved.values())

# Expresiones regulares para tokens
t_EXIT = r'salir'

def t_CODE(t):
    r'[0-9][0-9]-[0-9]-[0-9]'
    t.value = str(t.value) # str() necesario?
    return t

def t_KW(t):
    r'[a-z]+'
    t.type = reserved.get(t.value, 'KW')
    return t
    
t_ignore = ' \t'

# necesario?
def t_error(t):
    print("Error de caracter")
    t.lexer.skip(1) #esto hace que cuando hay un error no se cierre el programa (saltamos skip(n) caracteres)

precedence = (('left', 'CODE', 'KW'),) # necesario?

respuestas = {
    'B': 'Bomba',
    'Q': 'Porta Escala',
    'H': 'Hazmat',
    'M': 'Escala',
    'R': 'Rescate'
}

def p_respuesta(t):
    'respuesta : s'
    print(f'AyC {os.getcwd()}> {t[1]}')

def p_res_completa(t):
    's : CODE KW'
    if t[2] == 'riesgo':
        if t[1] == '10-0-1':
            t[0] = '3B 2Q 1H'
        elif t[1] == '10-0-2':
            t[0] = '3B 2Q 2M'
        elif t[1] == '10-4-1':
            t[0] = '1B 2R'
        elif t[1] == '10-4-2':
            t[0] = '2B 2R'
    elif t[2] == 'tranqui':
        if t[1] == '10-0-1':
            t[0] = '2B 1Q'
        elif t[1] == '10-0-2':
            t[0] = '2B 1Q 1M'
        elif t[1] == '10-4-1':
            t[0] = '1B 1R'
        elif t[1] == '10-4-2':
            t[0] = '2R 1B'

def p_exit(t):
    's : EXIT'
    if t[1] == 'salir':
        print(f'AyC {os.getcwd()}> Saliendo del interprete...')
        exit()

def p_error(t):
    if t is None:
        print("Syntax error: Unexpected end of input")
    else:
        print(f"Syntax error at token '{t.value}' (type: {t.type}), line {t.lineno}, position {t.lexpos}")



lexer = lex.lex()
parser = yacc.yacc()
print(f'AyC {os.getcwd()}> \nGlosario:')
for pair in respuestas.items():
    print(f'\t{pair[0]}: {pair[1]}'.expandtabs(4))
while True:
    try:
        data = input(f'AyC {os.getcwd()}> ')
    except EOFError:
        break
    parser.parse(data)
