from pickle import FALSE
import numpy as np

# objective is Z


def simplex(objective, restrictions, variables, maximize):
    objective_np = np.array(objective)
    objective_np = objective_np.astype(np.float64)

    restrictions_np = np.array(restrictions)
    restrictions_np = restrictions_np.astype(np.float64)

    # c array is not always 0
    c_array = np.zeros(len(restrictions))
    zj_array = np.zeros(len(variables))
    z_minus_zj_array = np.zeros(len(variables))

    for i in range(len(restrictions_np)):
        multip_array = np.multiply(c_array, restrictions_np[:, i])
        zj_array[i] = np.sum(multip_array)

    z_minus_zj_array = objective[:] - zj_array[:]
    print(z_minus_zj_array)


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


print(is_solution([0, 0, -1, 0, 0], False))
