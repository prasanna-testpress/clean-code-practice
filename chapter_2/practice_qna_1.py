#Question 1
def d(n, t):
    for x in n:
        if x > t:
            print("Alert:", x)


#my answer

def detect_action(temperatures,average_temperature):

    for temp in temperatures:

        if temp >average_temperature:
            return temp
    return None     



#Refactor

from typing import List, Optional

def find_temperature_exceeding_average(
    temperatures: List[float],
    average_temperature: float
) -> Optional[float]:
    """Return the first temperature reading that exceeds the average, or None if all are below."""
    for temperature in temperatures:
        if temperature > average_temperature:
            return temperature
    return None
