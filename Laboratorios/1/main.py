
import math_simplex
import sys

def main():
  math_simplex.simplex_solver("x1 + 4x2", ["-10x1 + 20x2 <= 22", "5x1 + 10x2 <= 49", "x1 >= 4", "x2 <= 2"], True)

if __name__ == "__main__":
    main()