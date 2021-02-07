from art import logo
def add(n1, n2):
  '''Cong 2 so'''
  return n1 + n2

def sub(n1, n2):
  '''Tru 2 so'''
  return n1 - n2

def div(n1, n2):
  '''Chia 2 so'''
  return n1 / n2

def mul(n1, n2):
  '''Nhan 2 so'''
  return n1 * n2

operations = { 
  '+' : add,
  '-' : sub,
  '/' : div,
  '*' : mul
}
def calculator():
  print(logo)
  num1 = float(input("What's the first number ? : "))
  for operation in operations:
    print(operation)

  should_continue = 1
  while (should_continue):
    operations_symbol = input("Pick an operations: ")
    num2 = float(input("What's the next number: "))
    calculation_function = operations[operations_symbol]
    answer1 = calculation_function(num1, num2)
    print(f"{num1} {operations_symbol} {num2} = {answer1}")
    flag = input(f"Type 'y' to continue calculating with {answer1}, or type 'n' to make new calculation: ")
    if flag.lower() ==  'y' :
      num1 = answer1
    else:
      should_continue = 0
      calculator()

calculator()
  
