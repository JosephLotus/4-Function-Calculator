logo = """
 _____________________
|  _________________  |
| | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|
"""

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

calculator_operations = {
    '+' : add,
    '-' : subtract,
    '*' : multiply,
    '/' : divide,
}

def calculator():
    print (logo)
    calculations_complete = False
    num_1 = float(input("What is the first number?: "))
    while not calculations_complete:
        for operator in calculator_operations:
            print (operator)
        operator_choice = input("Choose an operator from above: ")
        num_2 = float(input("What is the next number?: "))
        calculation = calculator_operations[operator_choice]
        answer = calculation(num_1, num_2)
        print (f"{num_1} {operator_choice} {num_2} = {answer}")
        should_continue = input(f"Type 'y' to continue calculating with {answer}, "
                                f"or type 'n' to start a new calculation: ")
        if should_continue == "n":
            calculations_complete = True
            calculator()
        else:
            num_1 = answer

calculator()