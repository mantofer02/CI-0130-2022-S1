import parser_simplex
import sys

# def main():
#     print(f"Arguments: {sys.argv}")
    
#     if (len(sys.argv) < 2):
#         file_reader = FileReader()
#     else:
#         file_reader = FileReader(sys.argv[1])
#         if (sys.argv[-1] == '-v'):
#             file_reader.verbose_mode()

# def main():
#     if(len(sys.argv) == 1):
#         equation = input()
#         # print(equation)
#         n = input("Ingrese cantidad de restricciones")
#         restriction = []
#         while(n != 0):
#             restriction.append(input())
#             n -= 1
#     else:
#         with open('equation.txt') as f:
#             lines = f.readlines()

def main():
  #print(parser_simplex.parse_equation("-3.8x1 + 5x2 -2x3 + x4 -9x5"))
  restriction = "-3.8x1 + 5x2 -2x3 + x4 -9x5 >= 23"
  print(parser_simplex.parse_restriction(restriction))

if __name__ == "__main__":
    main()