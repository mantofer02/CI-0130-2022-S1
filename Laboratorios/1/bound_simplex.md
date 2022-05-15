First the input for the main function was changed to:"x1 + 4x2", ["-10x1 + 20x2 <= 22", "5x1 + 10x2 <= 49", "x1 <= 5"], True
Then, the answer came out to be:([('x2', 3.0), ('x1', 3.8), ('s3', 1.2000000000000002)], 15.8)
So we decided to bound the x1 values upwards and downwards. x1 <= 3 and x1 >= 4
When added, the restriction x1 <= 3 the results are the following: ([('x2', 2.6), ('s2', 8.0), ('s3', 2.0), ('x1', 3.0)], 13.4)
When added, the restriction x1 >= 4 the results are the following: ([('s1', 4.0), ('x2', 2.9), ('s3', 1.0), ('x1', 4.0)], 15.6)

Since the answer is not a whole number, we will proceed to try with the other x2 bounded values:  x2 <= 2 and x2 >= 3