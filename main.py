from art import logo
#MY Calculator
#Addition
def add(num1, num2):
  return num1+num2

#Multiplication
def multiply(num1, num2):
  return num1*num2

#Substraction
def substract(num1, num2):
  return num1-num2

#Divide
def divide(num1, num2):
  return num1/num2

operations = {"+": add , "-": substract, "*": multiply, "/": divide}
def calculator():  
  print(logo)

  num1 = float(input("Enter a number: "))
  
  for operator in operations:
    print(operator)
  running = True

  while running:
    symbol = input("Which operation do you want to perform? ")
    num2 = float(input("Enter the next number: "))
    calculate = operations[symbol]
    answer = calculate(num1, num2)
    print(f"{num1} {symbol} {num2} = {answer}")
  
    run = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to exit:")
    if run == 'y':
      num1 = answer
    elif run == 'n':
      running = False
      calculator()


calculator()
  
