alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
number = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
operator = ['+', '-', '*', '/', '=']
functions = ['sqrt', 'sin', 'cos', 'tan']
variables = ['pi']


#expression lexer function
def lexer(input_str):
    input_str = input_str + " "
    out_char = ""
    expression = []
    tokens = []

    for x in range(len(input_str)):
        char = input_str[x]
        if char in alpha:
            out_char = out_char+char

        elif char in number:
            out_char = out_char+char

        elif char == "+" or char == "-" or char == "*" or char == "/" or char == "^" or char == "=":
            expression.append(out_char)
            out_char = ""
            out_char = out_char+char
            expression.append(out_char)
            out_char=""
        
        elif char.isspace():
            expression.append(out_char)
            out_char = ""

        elif char == "(" or char == ")":
            expression.append(out_char)
            out_char = ""
            out_char = out_char+char
            expression.append(out_char)
            out_char = ""

        
          
    return expression

