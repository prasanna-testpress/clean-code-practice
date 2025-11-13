#Question 2
def calculate(x, y, z):
    if z == 1:
        print("Sum:", x + y)
    elif z == 2:
        print("Product:", x * y)
    else:
        print("Invalid")


#my anwser
def perform_calculation(operands,operates: list[int])->string:

    match operands:

        case 1:
            return f"Sum:{operates[0]+operates[1]}"
        case 2:
            return f"Product:{operates[0]*operates[1]}"
        case _:
            return f"Invalid"