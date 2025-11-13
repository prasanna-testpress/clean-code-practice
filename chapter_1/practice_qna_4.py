#Question 4
def calc(x, y, op):
    if op == "a":
        print(x + y)
    elif op == "s":
        print(x - y)
    elif op == "m":
        print(x * y)
    elif op == "d":
        if y != 0:
            print(x / y)
        else:
            print("err")


# My answer
from enum import Enum

class Operation(Enum):
    ADD="a"
    SUBTRACT="s"
    MULTIPLY="m"
    DIVISION="d"

def perform_calculation(first_operand,second_operand,operators):

        if Operation.ADD == operators:
            return first_operand + second_operand
        elif Operation.SUBTRACT == operators:
            return first_operand - second_operand
        elif Operation.MULTIPLY == operators:
            return first_operand * second_operand
        elif Operation.DIVISION == operators:
            if second_operand != 0:
                return first_operand / second_operand
            else:
                raise "second operand can not be zero"