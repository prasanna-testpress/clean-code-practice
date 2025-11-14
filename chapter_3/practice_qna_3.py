#Question 1
def format_user(user, detailed):
    result = f"{user['name']} ({user['id']})"
    
    if detailed:
        result += f" - email: {user['email']}, phone: {user['phone']}"

    return result


#my answer

from enum import Enum

class User(Enum):
    NAME:"name"
    ID:"id"
    EMAIL:"email"
    PHONE:"phone"



def format_user_summary(user:dict[str,str]):
    """Return the shorter version of user data"""

    return f"name: {user[User.NAME]} - id: {User.NAME}"

def format_detailed_user_summary(user:dict[str,str]):
    """Return the Detailed version of user data"""

    return f"name: {user[User.NAME]} - id: {User.NAME} - emil :{User.EMAIL} - phone: {User.PHONE}"




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
