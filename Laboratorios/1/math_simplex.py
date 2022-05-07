import numpy as np

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

