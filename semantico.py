from lexico import tokens
from sintactico import parser, names

variables = {}
functions = {}
semantic_errors = []

def analyze_semantics(ast):
    global variables, functions, semantic_errors
    variables = {}
    functions = {}
    semantic_errors = []
    visit(ast)
    if len(semantic_errors) == 0:
        return "Análisis semántico completado sin errores."
    else:
        errors_str = "Se encontraron los siguientes errores semánticos:\n" + "\n".join(semantic_errors)
        return errors_str

def visit(node):
    if isinstance(node, dict):
        if 'type' in node:
            if node['type'] == 'var_declaration':
                var_name = node['name']
                var_type = node['value']['type']
                if var_name in variables:
                    semantic_errors.append(f"Error semántico: La variable '{var_name}' ya ha sido declarada.")
                else:
                    variables[var_name] = var_type
            elif node['type'] == 'var_assignment':
                var_name = node['name']
                value_type = get_type(node['value'])
                if var_name not in variables:
                    semantic_errors.append(f"Error semántico: La variable '{var_name}' no ha sido declarada.")
                else:
                    var_type = variables[var_name]
                    if var_type != value_type:
                        semantic_errors.append(f"Error semántico: Asignación de tipo incompatible. La variable '{var_name}' es de tipo '{var_type}', pero se le está asignando un valor de tipo '{value_type}'.")
            elif node['type'] == 'function_declaration':
                func_name = node['name']
                if func_name in functions:
                    semantic_errors.append(f"Error semántico: La función '{func_name}' ya ha sido declarada.")
                else:
                    functions[func_name] = node
            elif node['type'] == 'function_call':
                func_name = node['name']
                if func_name not in functions:
                    semantic_errors.append(f"Error semántico: La función '{func_name}' no ha sido declarada.")
                else:
                    func_node = functions[func_name]
                    if len(node.get('arguments', [])) != len(func_node['params']):
                        semantic_errors.append(f"Error semántico: El número de argumentos en la llamada a la función '{func_name}' no coincide con la declaración.")
                    else:
                        for arg, param in zip(node.get('arguments', []), func_node['params']):
                            arg_type = get_type(arg)
                            param_type = param if isinstance(param, str) else param['type']
                            if arg_type != param_type:
                                semantic_errors.append(f"Error semántico: Tipo de argumento incompatible en la llamada a la función '{func_name}'. Se esperaba '{param_type}', pero se recibió '{arg_type}'.")
            elif node['type'] == 'binary_operation':
                left_type = get_type(node['left'])
                right_type = get_type(node['right'])
                if left_type != right_type:
                    semantic_errors.append(f"Error semántico: Operación binaria con tipos incompatibles. Se está intentando operar entre tipos '{left_type}' y '{right_type}'.")
            elif node['type'] == 'unary_operation':
                operand_type = get_type(node['operand'])
                if operand_type != 'number':
                    semantic_errors.append(f"Error semántico: Operación unaria con tipo incompatible. Se esperaba 'number', pero se recibió '{operand_type}'.")
            elif node['type'] == 'comparison':
                left_type = get_type(node['left'])
                right_type = get_type(node['right'])
                if left_type != right_type:
                    semantic_errors.append(f"Error semántico: Comparación con tipos incompatibles. Se está intentando comparar tipos '{left_type}' y '{right_type}'.")
            elif node['type'] == 'print':
                value_type = get_type(node['value'])
                if value_type not in ['number', 'string']:
                    semantic_errors.append(f"Error semántico: Tipo incompatible en la declaración 'print'. Se esperaba 'number' o 'string', pero se recibió '{value_type}'.")
            elif node['type'] == 'if':
                condition_type = get_type(node['condition'])
                if condition_type != 'boolean':
                    semantic_errors.append(f"Error semántico: Condición de tipo incompatible en la declaración 'if'. Se esperaba 'boolean', pero se recibió '{condition_type}'.")
            elif node['type'] == 'while':
                condition_type = get_type(node['condition'])
                if condition_type != 'boolean':
                    semantic_errors.append(f"Error semántico: Condición de tipo incompatible en la declaración 'while'. Se esperaba 'boolean', pero se recibió '{condition_type}'.")
            elif node['type'] == 'for':
                condition_type = get_type(node['condition'])
                if condition_type != 'boolean':
                    semantic_errors.append(f"Error semántico: Condición de tipo incompatible en la declaración 'for'. Se esperaba 'boolean', pero se recibió '{condition_type}'.")
            elif node['type'] == 'return':
                return_type = get_type(node['value'])
        for child in node.values():
            visit(child)
    elif isinstance(node, list):
        for child in node:
            visit(child)

def get_type(node):
    if isinstance(node, dict):
        if 'type' in node:
            if node['type'] == 'number':
                return 'number'
            elif node['type'] == 'string':
                return 'string'
            elif node['type'] == 'boolean':
                return 'boolean'
            elif node['type'] == 'variable':
                var_name = node['name']
                if var_name in variables:
                    return variables[var_name]
                else:
                    semantic_errors.append(f"Error semántico: La variable '{var_name}' no ha sido declarada.")
                    return 'error'
            elif node['type'] == 'binary_operation':
                left_type = get_type(node['left'])
                right_type = get_type(node['right'])
                if left_type == right_type:
                    return left_type
                else:
                    return 'error'
            elif node['type'] == 'unary_operation':
                return get_type(node['operand'])
            elif node['type'] == 'comparison':
                left_type = get_type(node['left'])
                right_type = get_type(node['right'])
                if left_type == right_type:
                    return 'boolean'
                else:
                    return 'error'
    return 'error'

# Prueba
data = '''# Inicialización de variables
ITEM health = 100;
ITEM enemyHealth = 150;
ITEM damage = 5;
ITEM hola = "hola";

# Definición de función
CODEC attack() {    
    enemyHealth = enemyHealth - "hey";
    PRINT("Vida del enemigo reducida a: ");
    SCAN (enemyHealth <= 0) {
        PRINT("Enemigo eliminado");
    }
}

SUMMON attack();
'''
def analizar_semantica(data):
    ast = parser.parse(data)
    results = analyze_semantics(ast)
    return results
ast = parser.parse(data)
analyze_semantics(ast)