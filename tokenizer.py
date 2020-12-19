import lexer

alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
number = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
operator = ['+', '-', '*', '/', '=']
functions = ['sqrt', 'sin', 'cos', 'tan']

operations = []
terms = []
lexed = []

class term():
  def __init__(self, var, coefficient, degree):
    self.var = var
    self.coefficient = coefficient
    self.degree = degree

class operation():
  def __init__(self, operation):
    self.operation = operation

def sort(lexed):
  operations = []
  terms = []
  for x in range(len(lexed)):
    element = lexed[x]
    if element in operator or element in functions:
      operations.append(element)

    if element not in operator or element not in functions:
      vars = []
      coefficient = ""
      degree = ""
      for i in range(len(element)):
        char = element[i]
        if char in alpha:
          vars.append()


  
  