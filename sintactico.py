import ply.yacc as yacc
from lexico import tokens

precedence = (
    ('left', 'PLUS', 'MINUS'),
    ('left', 'TIMES', 'DIVIDE'),
    ('nonassoc', 'LT', 'LTE', 'GT', 'GTE', 'NE'),
    ('right', 'UMINUS'),
)

# diccionario para almacenar las variables
names = {}

results = ""

def p_program(p):
    '''program : program statement
               | statement'''
    if len(p) == 3:
        p[0] = p[1] + [p[2]]
    else:
        p[0] = [p[1]]

def p_statement_expr(p):
    'statement : expression SEMICOLON'
    p[0] = {'type': 'expression', 'value': p[1]}

def p_statement_assign(p):
    '''statement : VAR ID ASSIGN expression SEMICOLON
                 | ID ASSIGN expression SEMICOLON'''
    if len(p) == 6:
        p[0] = {'type': 'var_declaration', 'name': p[2], 'value': p[4]}
    else:
        p[0] = {'type': 'var_assignment', 'name': p[1], 'value': p[3]}

def p_statement_function(p):
    '''statement : FUNCTION ID LPARENT RPARENT block
                 | FUNCTION ID LPARENT VAR ID RPARENT block'''
    if len(p) == 6:
        p[0] = {'type': 'function_declaration', 'name': p[2], 'params': [], 'body': p[5]}
    elif len(p) == 8:
        param_type = p[4]
        param_name = p[5]
        p[0] = {'type': 'function_declaration', 'name': p[2], 'params': [(param_name, param_type)], 'body': p[7]}

def p_statement_if(p):
    'statement : IF LPARENT expression RPARENT block'
    p[0] = {'type': 'if', 'condition': p[3], 'body': p[5]}

def p_statement_while(p):
    'statement : WHILE LPARENT expression RPARENT block'
    p[0] = {'type': 'while', 'condition': p[3], 'body': p[5]}

def p_statement_for(p):
    'statement : FOR LPARENT statement SEMICOLON expression SEMICOLON expression RPARENT block'
    p[0] = {'type': 'for', 'init': p[3], 'condition': p[5], 'step': p[7], 'body': p[9]}

def p_statement_return(p):
    'statement : RETURN expression SEMICOLON'
    p[0] = {'type': 'return', 'value': p[2]}

def p_block(p):
    '''block : LBRACE statements RBRACE
             | LBRACE RBRACE'''
    if len(p) == 4:
        p[0] = p[2]
    else:
        p[0] = []

def p_statements(p):
    '''statements : statements statement
                  | statement'''
    if len(p) == 3:
        p[0] = p[1] + [p[2]]
    else:
        p[0] = [p[1]]

def p_expression_binop(p):
    '''expression : expression PLUS expression
                  | expression MINUS expression
                  | expression TIMES expression
                  | expression DIVIDE expression'''
    p[0] = {'type': 'binary_operation', 'operator': p[2], 'left': p[1], 'right': p[3]}

def p_expression_uminus(p):
    'expression : MINUS expression %prec UMINUS'
    p[0] = {'type': 'unary_operation', 'operator': '-', 'operand': p[2]}

def p_expression_group(p):
    'expression : LPARENT expression RPARENT'
    p[0] = p[2]

def p_expression_number(p):
    'expression : NUMBER'
    p[0] = {'type': 'number', 'value': p[1]}

def p_expression_name(p):
    'expression : ID'
    p[0] = {'type': 'variable', 'name': p[1]}

def p_expression_comparison(p):
    '''expression : expression LT expression
                  | expression LTE expression
                  | expression GT expression
                  | expression GTE expression
                  | expression NE expression'''
    p[0] = {'type': 'comparison', 'operator': p[2], 'left': p[1], 'right': p[3]}

def p_expression_string(p):
    'expression : STRING'
    p[0] = {'type': 'string', 'value': p[1]}

def p_statement_print(p):
    'statement : PRINT LPARENT expression RPARENT SEMICOLON'
    p[0] = {'type': 'print', 'value': p[3]}

def p_statement_summon(p):
    'statement : CALL ID LPARENT arguments RPARENT SEMICOLON'
    p[0] = {'type': 'function_call', 'name': p[2], 'arguments': p[4] if p[4] != [None] else []}

def p_arguments(p):
    '''arguments : arguments COMMA expression
                 | expression
                 | empty'''
    if len(p) == 2:
        p[0] = [p[1]]
    elif len(p) > 2:
        p[1].append(p[3])
        p[0] = p[1]
    else:
        p[0] = []

def p_empty(p):
    'empty :'
    pass

def append_result(message):
    global results
    results += message + "\n"

def p_error(p):
    if p:
        append_result(f"Error de Sintaxis en '{p.value}' en la línea {p.lineno}")
        print(f"Error de Sintaxis en '{p.value}' en la línea {p.lineno}")
    else:
        aux = "Error de Sintaxis al final del código"
        append_result(aux)
        print(aux)

parser = yacc.yacc(debug=False)

def analizar_sintactico(data):
    global results
    results = ""
    ast = parser.parse(data, debug=False)
    return results

# Prueba
data = '''# Inicialización de variables
ITEM health = 100;
ITEM enemyHealth = 150;
ITEM damage = 5;

# Definición de función
CODEC attack() {
    enemyHealth = enemyHealth - damage;
    PRINT("Vida del enemigo reducida a: ");
    SCAN (enemyHealth <= 0) {
        PRINT("Enemigo eliminado");
    }
}

SUMMON attack();
'''

if __name__ == '__main__':
    ast = parser.parse(data)
    print(ast)