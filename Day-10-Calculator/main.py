from art import logo
print(logo)
def add(n1, n2):
  return n1 + n2

def subtract(n1, n2):
  return n1 - n2

def multiply(n1, n2):
  return n1 * n2

def divide(n1, n2):
  return n1 / n2

def remainder(n1, n2):
  return n1%n2

operations = {
  "+": add,
  "-": subtract,
  "*": multiply,
  "/": divide,
  "%": remainder
}

def calculator():
  num1 = float(input("What's the first number?: "))
  for symbol in operations:
    print(symbol)

  should_continue = True
  while should_continue:
  #Here we select "+"
    operation_symbol = input("Pick an operation: ") 
    while not operation_symbol in operations:
        print("You choose invalid operator")
        operation_symbol = input("Please choose another valid operation above: ")

    num2 = float(input("What's the next number?: "))
    calculation_function = operations[operation_symbol]
    answer = calculation_function(num1, num2)

    print(f"{num1} {operation_symbol} {num2} = {answer}")

    continue_cal = input(f"Type 'y' to continue calculating with {answer}. Type 'n' to start a new calculator : ").lower()
    if continue_cal == "y":
      num1 = answer
    else:
      should_continue = False
      calculator()
  
calculator()