import math


def extract_function(_input):
    x_list = _input.split()
    var_list = []
    value_dic = {'variables': var_list, 'const': 0}
    for i in x_list:
        try:
            a, n = i.split('x')

            if a is '' or n is '':
                if a is '':
                    a = 1
                if n is '':
                    n = 1

            var_list.append({'a': float(a), 'n': float(n)})
        except ValueError as e:
            value_dic['const'] = float(i)

    return value_dic


def derivative_function(original_func_val):
    var_list = []
    derivatived_dic = {'variables': var_list, 'const': 0}
    a = 0
    n = 0
    for i in original_func_val['variables']:
        a = i['a'] * i['n']
        n = i['n'] - 1
        var_list.append({'a': a, 'n': n})

    return derivatived_dic


def execute_function(func_val_dic, x):
    y = func_val_dic['const']

    for a_n in func_val_dic['variables']:
        y += a_n['a'] * math.pow(x, a_n['n'])

    return y


def grape_to_string(grape):
    stringed = ''
    for i in grape['variables']:
        stringed += str(i['a']) + 'x' + str(i['n']) + ' '
    if grape['const'] != 0:
        stringed += str(grape['const'])
    return stringed






