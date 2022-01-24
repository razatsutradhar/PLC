from LISPParser import parser

def eval_expression(tree):
    # print(tree)
    if tree[0] == 'num':
        return tree[1]
    elif tree[0] == 'bool':
        return tree[1]
    elif tree[0] == 'id':
        return 'ERROR: Cannot evaluate ID ' + tree[1]
    elif tree[0] == '+' or tree[0] == '-' or tree[0] == '*' or tree[0] == '/' or tree[0] == '<'  or tree[0] == '>'or tree[0] == 'or' or tree[0] == 'and':
        print(tree[0])
        v1 = eval_expression(tree[1])
        if isinstance(v1, str):
            return v1
        v2 = eval_expression(tree[2])
        if isinstance(v2, str):
            return v2
        if tree[0] == '+':
            return v1 + v2
        elif tree[0] == '-':
            return v1 - v2
        elif tree[0] == '*':
            return v1 * v2
        elif tree[0] == '<':
            return bool(v1 < v2)
        elif tree[0] == '>':
            return bool(v1 > v2)
        elif tree[0] == 'or':
            return bool(v1 or v2)
        elif tree[0] == 'and':
            return bool(v1 and v2)
        elif v2 != 0 and tree[0] == '/':
            return v1 / v2
        else:
            return 'ERROR: Divide by Zero'
    elif tree[0] == 'if':
        v1 = eval_expression(tree[1])
        if v1:
            return eval_expression(tree[2])
        else:
            return eval_expression(tree[3])
    elif tree[0] == 'list':
        print("Tree" + tree)
    else:  # with clause
        return "WITH not implemented!"


def read_input():
    result = ''
    while True:
        data = input('WAE: ').strip()
        if ';' in data:
            i = data.index(';')
            result += data[0:i + 1]
            break
        else:
            result += data + ' '
    return result


def main():
    while True:
        data = read_input()
        if data == 'exit;':
            break
        try:
            tree = parser.parse(data)
        except Exception as inst:
            print(inst.args[0])
            continue
        try:
            answer = eval_expression(tree)
            if isinstance(answer, str):
                print('\nEVALUATION ERROR: ' + answer + '\n')
            else:
                print('\nThe value is ' + str(answer) + '\n')
        except Exception as inst:
            print(inst.args[0])


main()