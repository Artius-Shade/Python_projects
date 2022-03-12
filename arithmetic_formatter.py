def arithmetic_arranger(problems, arg2=False):

  if len(problems) > 5:
    return 'Error: Too many problems.'
  line1, line2, line3, line4 = [[], [], [], []]
  for problem in problems:
    pl = problem.split()
    operator = pl[1]
    if operator != '+' and operator != '-':
      return "Error: Operator must be '+' or '-'."
    try:
      num1, num2 = int(pl[0]), int(pl[2])
    except:
      return "Error: Numbers must only contain digits."
    if len(str(num1)) > 4 or len(str(num2)) > 4:
      return "Error: Numbers cannot be more than four digits."

    if operator == '+':
      result = num1 + num2
    else:
      result = num1 - num2
    longest = max(len(str(num1)), len(str(num2)))
    ostr = f"{operator} " + " " * longest
    x = len(ostr) - len(str(num2))
    l2 = ostr[:x] + str(num2)
    l1 = (" " * (len(l2) - len(str(num1)))) + str(num1)
    l3 = "-" * len(l2)
    l4 = (" " * (len(l2) - len(str(result)))) + str(result)
    line1.append(l1)
    line2.append(l2)
    line3.append(l3)
    line4.append(l4)
  line1 = '    '.join(line1)
  line2 = '    '.join(line2)
  line3 = '    '.join(line3)
  line4 = '    '.join(line4)
  if arg2:
    arranged_problems = f"{line1}\n{line2}\n{line3}\n{line4}"
    return arranged_problems
  else:
    arranged_problems = f"{line1}\n{line2}\n{line3}"
    return arranged_problems
