def p(a, b, c):
    if a:
        if b:
            print("ok")
        else:
            if c:
                print("maybe")
            else:
                print("no")


def prediction(a,b,c):

    if not a:
        return
    
    if  b:
        return "ok"
    
    if c:
        return "maybe"
    
    return "no"

from enum import Enum

class Prediction(str, Enum):
    OK = "ok"
    MAYBE = "maybe"
    NO = "no"

def predict_outcome(condition_met: bool, secondary_check: bool, fallback_check: bool) -> Prediction | None:
    """Return the prediction outcome based on provided boolean conditions."""
    if not condition_met:
        return None

    if secondary_check:
        return Prediction.OK

    if fallback_check:
        return Prediction.MAYBE

    return Prediction.NO
