# @param:
#   equation: -3.8x1 + 5x2 -2x3
# @output: 'x1': -3.8, 'x2': 5.0, 'x3': -2.0
def parse_equation(equation):
    dict = {}
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
    parsed_restrictions = []
    coef_array = []

    for key in parsed_eq:
        coef_array.append(key)

    for i in range(len(restrictions)):
        coef_array.append("s" + str(i + 1))
        parsed_restrictions.append(parse_restriction(restrictions[i]))

    for i in range(len(restrictions)):
        if parsed_restrictions[i][2] == False:
          coef_array.append("a" + str(i + 1))
    print(coef_array)


parse_problem("30x1 + 100x2", ["x1 + x2 <= 7",
              "4x1 + 10x2 <= 40", "10x1 >= 30"], True)
