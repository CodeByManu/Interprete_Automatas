import ply.lex as lex
import ply.yacc as yacc

# palabra_reservada: TOKEN
reserved = {
    # 'riesgo': 'RIESGO',
    # 'tranqui': 'TRANQUI',
    'salir': 'EXIT',
    # ' ': 'WHITESPACE'
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
# t_RIESGO = r'riesgo'
# t_TRANQUI = r'tranqui'
t_EXIT = r'salir'
# t_WHITESPACE = r' '

def t_CODE(t):
    r'[0-9][0-9]-[0-9]-[0-9]'
    t.value = str(t.value) # str() necesario?
    return t

def t_KW(t):
    # r'(riesgo|tranqui)' #incluir espacio previo?
    r'[a-z]+'
    t.type = reserved.get(t.value, 'KW')
    return t
    
t_ignore = ' \t'

# necesario?
def t_error(t):
    print("Error de caracter")
    t.lexer.skip(1) #esto hace que cuando hay un error no se cierre el programa (saltamos skip(n) caracteres)

precedence = (('left', 'CODE', 'KW'),) # necesario?

# pendiente = {}
respuestas = {
    'B': 'Bomba',
    'Q': 'Escala',
    'H': '',
    'M': 'Mecanica',
    'R': ''
}

def p_respuesta(t):
    'respuesta : s'
    print(t[1])

# def p_res_es(t):
#     'respuesta : CODE KW'

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

# def p_res_code(t):
#     's : CODE'
#     t[0] = t[1]
#     pendiente[t[1]] = ''
#     print('Especifique tipo para el siguiente codigo ingresado:')
    
# def p_res_kw(t):
#     's : KW'
#     if pendiente.keys() and t[1] == ('riesgo' or 'tranqui'):
#         pendiente[pendiente[-1]] = t[1]
#         t[0] = t[1]

# def p_tipo(t):
#     'tipo : KW'


# def p_respuesta(t):
#     'respuesta : CODE KW'
#     if t[3] == 'riesgo':
#         if t[1] == '10-0-1':
#             print('3B 2Q 1H')
#         elif t[1] == '10-0-2':
#             print('3B 2Q 2M')
#         elif t[1] == '10-4-1':
#             print('1B 2R')
#         elif t[1] == '10-4-2':
#             print('2B 2R')
#     elif t[3] == 'tranqui':
#         if t[1] == '10-0-1':
#             print('2B 1Q')
#         elif t[1] == '10-0-2':
#             print('2B 1Q 1M')
#         elif t[1] == '10-4-1':
#             print('1B 1R')
#         elif t[1] == '10-4-2':
#             print('2R 1B')

def p_exit(t):
    's : EXIT'
    if t[1] == 'salir':
        print('terminando el programa...')
        exit()
# def p_expr_num(t):
#     's : N'
#     t[0]=t[1]
    
# def p_expr_id(t):
#     's : ID'
#     try:
#         t[0] = pairs[t[1]]
#     except LookupError:
#         print("Variable indefinida '%s'" % t[1])
#         t[0] = 0
    
# def p_expr_op(t):
#     '''s : CODE KW'''
#     if t[2] == 'riesgo':
#         t[0]=t[1]+t[3]
#     elif t[2] == 'tranqui':
#         t[0]=t[1]-t[3]

def p_error(t):
    if t is None:
        print("Syntax error: Unexpected end of input")
    else:
        print(f"Syntax error at token '{t.value}' (type: {t.type}), line {t.lineno}, position {t.lexpos}")



lexer = lex.lex()
parser = yacc.yacc()
while True:
    try:
        data = input()
        # if data == 'salir':
        #     print('terminando el programa...')
        #     break
    except EOFError:
        break
    parser.parse(data)
