import operator

def arithmetic_arranger(problems, perform = False):
  arranged_problems = ""
  if len(problems) > 5:
    return "Error: Too many problems."
  left_operand = []
  right_operand = []
  operator_list = []
  operators = {'+': operator.add, '-': operator.sub}
  for entry in problems:
    if any(a.isalpha() for a in entry):
      return "Error: Numbers must only contain digits."
    item = entry.split(' ')
    if item[1] in operators.keys():
      operator_list.append(item[1])
    else:
      return "Error: Operator must be '+' or '-'."
    if len(item[0]) > 4:
      return "Error: Numbers cannot be more than four digits."
    else:
      left_operand.append(item[0])
    if len(item[2]) > 4:
      return "Error: Numbers cannot be more than four digits."
    else:
        right_operand.append(item[2])
  #print("lefties: ", left_operand)
  #print("righties: ", right_operand)
  #print("lefties: ", operator_list)

  list_length = len(left_operand)
  
  if all(len(lst) == list_length for lst in [left_operand, operator_list, right_operand]):
    first_row = ""
    second_row = ""
    third_row = ""
    fourth_row = ""
    for i in range(list_length):
      max_length = max(len(left_operand[i]),len(right_operand[i]))
      #first line
      first_row_space = max_length - len(left_operand[i])
      first_row += "  " + (" "*first_row_space) + left_operand[i]
      if i < (list_length - 1):
        first_row += " "*4
      
      #second line
      second_row_space = max_length - len(right_operand[i])
      second_row += operator_list[i] + " " + (" "*second_row_space) + right_operand[i]
      if i < (list_length - 1):
        second_row += " "*4
      #third line
      third_row += "--" + ("-"*max_length)
      if i < (list_length - 1):
        third_row += " "*4

      #fourth line
      if perform:
        result = str(operators[operator_list[i]](int(left_operand[i]), int(right_operand[i])))
        result_row_space = (max_length + 2) - len(result)
        fourth_row +=" "*result_row_space + result
        if i < (list_length - 1):
          fourth_row += " "*4

    arranged_problems += first_row
    arranged_problems += "\n"
    arranged_problems += second_row
    arranged_problems += "\n"
    arranged_problems += third_row
    if perform:
      # print(fourth_row)
      arranged_problems += "\n"
      arranged_problems += fourth_row
  else:
    print("lists have different lengths")
    
  return arranged_problems
