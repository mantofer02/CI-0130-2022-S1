
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
  if ">=" in restriction:
    string1, string2 = restriction.split(">=")
    check = False
  elif "<=" in restriction:
    string1, string2 = restriction.split("<=")
    check = True
  dict[0] = parse_equation(string1.rstrip())
  lista = [dict[0], string2.lstrip(), check ]
  return lista
  