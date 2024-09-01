from art import logo
print(logo)

def add(n1, n2):
    return n1 + n2

#TODO: Write out the other 3 functions
def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2


#TODO : Add these 4 functions to a dictionary, keys = "+", "-", "*", "/"

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}


#TODO: Use the dictionary operations to perform the calculations. Multiply 4 * 8
#print(operations["*"](4,8))

program_running = True

while program_running:
    continue_with_prev = True
    first_num = float(input("What's the first number?"))
    while continue_with_prev:
        operation = input("""+
-
*
/
Pick an operation:
""")
        second_num = float(input("What's the next number?"))
        result = operations[operation](first_num, second_num)
        print(f"{first_num} {operation} {second_num} = {result}")
        continue_calculating = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation")
        if continue_calculating == 'n':
            continue_with_prev = False
        else:
            first_num = result

