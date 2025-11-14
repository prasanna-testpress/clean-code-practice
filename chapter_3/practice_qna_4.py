#Question 4
def format_user_summary(user:dict[str,str]):
    """Return the shorter version of user data"""
    return f"name: {user['name']} - id: {user['id']}"

def format_detailed_user_summary(user:dict[str,str]):
    """Return the Detailed version of user data"""
    return f"name: {user['name']} - id: {user['id']} - email: {user['email']} - phone: {user['phone']}"



#my answer

def format_user_summary(user:dict[str,str]):
    """Return the shorter version of user data"""
    return f"name: {user['name']} - id: {user['id']}"

def format_detailed_user_summary(user:dict[str,str]):
    """Return the Detailed version of user data"""
    return f"{format_user_summary(user)} - email: {user['email']} - phone: {user['phone']}"

 



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
