# CI-0130-2022-S1 | Laboratory 1 | Bound Simplex

- [CI-0130-2022-S1 | Laboratory 1 | Bound Simplex](#ci-0130-2022-s1--laboratory-1--bound-simplex)
  - [Simplex method with bounding](#simplex-method-with-bounding)
  - [LP Tree](#lp-tree)

## Simplex method with bounding

In this section, we will execute a maximization function with its respective constraints through the simplex method. Then analize if the results are whole numbers, if they are not we will rerun the program with its respective bounding. This new values for restrictions are decided by bounding towards the closest integer upwards and downwards. For example if we want to bound the number 5.1 we would have to create arbitrary values for 5 and 6.

The example decided for this part was the following:
`Maximize z = x1 + 4x2` restrained by `-10x1 + 20x2 <= 22, 5x1 + 10x2 <= 49 + x1 <= 5`. If the solution does not have a whole number, the process has to be repeated by rebounding the variables.

- First LP solution

1. First, the input for the main function is changed to `("x1 + 4x2", ["-10x1 + 20x2 <= 22", "5x1 + 10x2 <= 49", "x1 <= 5"], True)`
2. The answer comes to: `([('x2', 3.0), ('x1', 3.8), ('s3', 1.2000000000000002)], 15.8)` which means that it is necessary to execute the algorithm again with different values `(x1 <= 3 and x1 >= 4)`.

- When `x1 <= 3`:
  
1. The restriction `x1 <= 3` is added to the list of restrictions and the solution is now: `([('x2', 2.6), ('s2', 8.0), ('s3', 2.0), ('x1', 3.0)], 13.4)`. Since the solution is not a whole number the process is repeated again with `x2 <= 2` and `x2 >= 3` as the new values.

- When `x2 <= 2`:

1. The solution for `x2 <= 2` comes out to be: `([('x2', 2.0), ('s2', 14.0), ('s3', 2.0), ('s1', 12.000000000000002), ('x1', 3.0)], 11.0)`
  
- When `x2 >=3`:

1. For `x2 >= 3` the solution is not a feasible solution so it gets ignored.

-When `x1 >= 4`:

1. The restriction `x1 >= 4` is added to the list of restrictions and the solution is now: `([('s1', 4.0), ('x2', 2.9), ('s3', 1.0), ('x1', 4.0)], 15.6)`. Since the solution is not a whole number the process is repeated again with `x2 <= 2` and `x2 >= 3` as the new values.

- When `x2 <= 2`

1. The solution for x2 <= 2 comes out to be: `([('s1', 32.0), ('s2', 4.0), ('s4', 1.0), ('x1', 5.0), ('x2', 2.0)], 13.0)`

- Wheb `x2 >= 3`:

1. For x2 >= 3 the solution is not a feasible solution so it gets ignored.

Then we proceed to analize the possible answers, and we can clearly see that best solution comes by adding the `x1 >= 4` and `x2 <= 2` restrictions. The values are `x1 = 5.0` and `x2 = 2.0` that comes to a solution `of 13.0`

## LP Tree

In the following graph, the process is shown more clearly. ![Binary Tree](https://i.imgur.com/JWm5lFf.jpg)
