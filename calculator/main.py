print("Welcome to calculator program")


def calculate_result(value1, value2, operator):
    if operator == "+":
        return value1 + value2
    elif operator == "-":
        return value1 - value2
    elif operator == "*":
        return value1 * value2
    elif operator == "/":
        return value1 / value2
    else:
        return -1


continue_calculation = True
result = 0
while continue_calculation:
    if result == 0:
        value_one = int(input("Enter a value one to be calculated: "))
    else:
        value_one = result
    chosen_operator = input("""
        Choose operator:
        + -> addition
        - -> subtraction
        * -> multiplication
        / -> division
    """)
    value_two = int(input("Enter a second value to be calculated"))
    result = calculate_result(value_one, value_two, chosen_operator)
    print(f"The result for the operation is: {result}")
    continue_operation = input(f"Would you like to continue the operation with the value {result}")
    if continue_operation == "yes":
        continue
    else:
        continue_calculation = False




