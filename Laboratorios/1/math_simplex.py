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


print(get_pivot_row([2, 3, 1], [400, 300, 90]))
