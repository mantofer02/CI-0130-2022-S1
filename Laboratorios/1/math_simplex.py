import numpy as np

def simplex(objective, restrictions, variables, maximize):
  objective_np = np.array(objective)
  objective_np = objective_np.astype(np.float64)

  restrictions_np = np.array(restrictions)
  restrictions_np = restrictions_np.astype(np.float64)