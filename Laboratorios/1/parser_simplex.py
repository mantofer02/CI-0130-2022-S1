M = 1000

def parse_equation(equation):
    dict = {}
    # print(equation)
    equation = equation.replace("+", " ")
    i = 1

    while equation:
        var = "x" + str(i)
        split = equation.split(var, 1)
        value = split.pop(0)
        value = value.replace(" ", "")
        if value == '':
            value = "1"
        elif value == '-':
            value = "-1"

        if len(split) > 0:
          dict[var] = value.split()[0]
          equation = split[0]
        i += 1
    return dict


def parse_restriction(restriction):
    dict = {}
    check = False
    opcode = ''
    if ">=" in restriction:
        opcode = ">="
    elif "<=" in restriction:
        opcode = "<="
        check = True

    string1, string2 = restriction.split(opcode)
    dict[0] = parse_equation(string1.rstrip())
    list = [dict[0], string2.lstrip(), check]
    return list


# @todo -> first and second array
def parse_problem(objective, restrictions, maximize):
    parsed_eq = parse_equation(objective)
    n_obj_var = len(parsed_eq)
    n_restrictions = len(restrictions)
    parsed_restrictions = []
    coeficients = []
    variables = []
    simplex_matrix = []

    for key in parsed_eq:
        variables.append(key)
        coeficients.append(float(parsed_eq.get(key)))

    for i in range(len(restrictions)):
        variables.append("s" + str(i + 1))
        coeficients.append(0)
        parsed_restrictions.append(parse_restriction(restrictions[i]))

    for i in range(len(restrictions)):
        if parsed_restrictions[i][2] == False:
            variables.append("a" + str(i + 1))
            coeficients.append(-1 * M) if maximize else coeficients.append(M)

    for i in range(n_restrictions):
        row = []
        restriction = parsed_restrictions[i][0]
        is_upper_bound = parsed_restrictions[i][2]
        for j in range(len(variables) + 1):
            value = restriction.get("x" + str(j + 1))
            if value:
                row.append(float(value))
            elif j == n_obj_var + i:
                row.append(1) if is_upper_bound else row.append(-1)
            elif j == len(variables):
                row.append(float(parsed_restrictions[i][1]))
            elif j == n_obj_var + n_restrictions + i:
                row.append(0) if is_upper_bound else row.append(1)
            else:
                row.append(0)
        simplex_matrix.append(row)

    return coeficients, simplex_matrix, variables
