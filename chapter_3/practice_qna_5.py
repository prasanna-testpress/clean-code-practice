#Question 1
def process_user(u, log=False, s=False):
    if u["status"] == "inactive":
        if s:
            u["status"] = "active"
        if log:
            print("User processed")
        return u
    else:
        if log:
            print("Already active")
        return u



#my answer

from typing import Dict,Any

def update_user_status(user:Dict[str,Any])->None:
    """Activate the status of the user"""
    user["status"]="active"

def is_active_status(user:Dict[str,Any])->bool:

    """Return true if the user is active"""
    return user["status"]=="active"

def display_to_user(content:str)->None:
    """Display the content to the user"""
    print(content)




