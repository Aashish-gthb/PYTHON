import os 
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

def add(n1,n2):
   return n1+n2

def subtract(n1,n2):
    return n1-n2

def multiply(n1,n2):
    return n1*n2

def division(n1,n2):
    return n1/n2

operations = { "+" : add,
              "-" : subtract,
              "*" : multiply,
              "/" : division }    
print(logo)   
def calculator():   
    num1 = float(input("what's the first no.?:"))

    for symbol in operations:
        print(symbol)

    go_again = False
    while not go_again : 
        operations_symbol = input("pick an operation:")
        num2 = float(input("what's the next no.?:"))

        calculation_function = operations[operations_symbol]
        answer = calculation_function(num1,num2)
        print(f"{num1}{operations_symbol}{num2} = {answer}")
        agian = input("type Y to continue  or N to end  or New to start a new calculation = ").lower()
        if  agian == 'n':
            go_again = True
            print(f"Your final answer: {answer}")
        if agian == 'y':
            num1 = answer    
        if agian == 'new':
            os.system('cls')
            calculator()
calculator()