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
        
# better anwser
from enum import Enum
from typing import List

class Operation(Enum):
    SUM = 1
    PRODUCT = 2

def perform_calculation(operation: Operation, numbers: List[int]) -> int:
    """Perform a calculation based on the given operation."""
    if operation == Operation.SUM:
        return sum(numbers)
    elif operation == Operation.PRODUCT:
        result = 1
        for n in numbers:
            result *= n
        return result
    else:
        raise ValueError("Invalid operation")
