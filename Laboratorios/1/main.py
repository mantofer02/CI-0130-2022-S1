
import math_simplex
import sys

def main():
  math_simplex.simplex_solver("0.65x1 + 0.45x2", ["2x1 + 3x2 <= 400", "3x1 + 1.5x2 <= 300", "x1 <= 90"], True)

if __name__ == "__main__":
    main()