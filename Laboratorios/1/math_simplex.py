import numpy as np

MAX_VAL = 10000

# objective is Z


def simplex(objective, restrictions, variables, maximize):
    objective_np = np.array(objective)
    objective_np = objective_np.astype(np.float64)

    restrictions_np = np.array(restrictions)
    restrictions_np = restrictions_np.astype(np.float64)

    # c array is not always 0
    c_array = np.zeros(len(restrictions))
    var_array = init_var_col(variables)
    # usa la expndida
    zj_array = np.zeros(len(variables) + 1)
    z_minus_zj_array = np.zeros(len(variables))

    for i in range(len(variables) + 1):
        multip_array = np.multiply(c_array, restrictions_np[:, i])
        zj_array[i] = np.sum(multip_array)

    z_minus_zj_array = objective[:] - zj_array[:]
    # print(z_minus_zj_array)

    if (not is_solution(z_minus_zj_array, maximize)):
        pivot_col = get_pivot_col(z_minus_zj_array, maximize)
        # vlaidate
        pivot_row = get_pivot_row(restrictions[:, pivot_col])
        pass


def is_solution(z_minus_zj_array, maximize):
    if maximize:
        for i in z_minus_zj_array:
            if i > 0:
                return False
        return True
    else:
        for i in z_minus_zj_array:
            if i < 0:
                return False
        return True


def get_pivot_col(z_minus_zj_array, maximize):
    if (maximize):
        return np.where(z_minus_zj_array == np.amax(z_minus_zj_array))[0][0]
    else:
        return np.where(z_minus_zj_array == np.amin(z_minus_zj_array))[0][0]


def get_pivot_row(column, b_row):
    ratio_row = np.copy(b_row)
    index = 0
    min_value = MAX_VAL
    for i in range(len(ratio_row)):
        if ratio_row[i] >= 0 and column[i] > 0:
            ratio_row[i] = ratio_row[i] / column[i]
            if (ratio_row[i]) < min_value:
                min_value = ratio_row[i]
                index = i
    return index


def init_var_col(variables):
    var_col = []
    for var in variables:
      if len(var.split("s")) > 1:
        var_col.append(var)
      if len(var.split("a")) > 1:
        index = int(var.split("a")[1])
        var_col[index - 1] = var
    return var_col

def init_c_col(var_col, objective, variables):
    var_col_index = 0
    c_array = np.zeros(len(var_col))
    for i in range(len(variables)):
        if variables[i] == var_col[var_col_index]:
          c_array[var_col_index] = objective[i]
          var_col_index += 1
    return c_array

get_pivot_row([2, 3, 1], [400, 300, 90])
var_col = init_var_col(["x1", "x2", "s1", "s2", "s3", "a3"])
print(init_c_col(var_col, [30.0, 100.0, 0, 0, 0, -10000], ["x1", "x2", "s1", "s2", "s3", "a3"]))