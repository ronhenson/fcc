from pickletools import read_stringnl_noescape_pair
from pydoc import stripid


def arithmetic_arranger(problems,is_answer=False):
     if len(problems) > 5:
          return "Error: Too many problems."
     top_row = ""
     bottom_row = ""
     dashes = ""
     answer_row =""
     four_spaces = " " * 4
     for problem in problems:
          
          # validate data
          if len(problem.split()) == 3:
               top_operand, operator, bottom_operand = problem.split()
          else:
               return "Error: Invalid number/operator format"
          if not top_operand.isdigit() or not bottom_operand.isdigit():
               return "Error: Numbers must only contain digits."   
          if len(top_operand) > 4 or len(bottom_operand) > 4:
               return  "Error: Numbers cannot be more than four digits."
          if "+" != operator and "-" != operator:
               return "Error: Operator must be '+' or '-'."
          
          # get width's and longest width of operands 
          top_len = len(top_operand)
          bottom_len = len(bottom_operand)
          width = max(top_len, bottom_len) + 2  # added 2 to include operator
          
          # row formatting
          top_row = (
               f'{top_row}'
               f'{" " * (width - top_len)}'
               f'{top_operand}'
               f'{four_spaces}'
          )
          bottom_row = (
               f'{bottom_row}'
               f'{operator}'
               f'{" " * (width - bottom_len - 1)}'
               f'{bottom_operand}'
               f'{four_spaces}'
          )
          dashes = f'{dashes}{"-" * width}{four_spaces}'
          if is_answer:
               ans = int(top_operand) + int(bottom_operand) \
                    if operator == "+" else int(top_operand) - int(bottom_operand)
               answer_row = (
                    f'{answer_row}'
                    f'{" " * (width - len(str(ans)))}'
                    f'{str(ans)}'
                    f'{four_spaces}'
               )
               
     # combine rows into one string          
     arranged_problems = (
          f'{top_row.rstrip()}\n'
          f'{bottom_row.rstrip()}\n'
          f'{dashes.rstrip()}'
     )
     if is_answer:
          arranged_problems = f'{arranged_problems}\n{answer_row.rstrip()}'
          
     return arranged_problems

