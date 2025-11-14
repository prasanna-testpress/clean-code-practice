#Question 2
def process_payment(user, amount, send_email):
    if user["balance"] < amount:
        print("Insufficient balance")
        return False

    user["balance"] -= amount

    print("Payment processed:", amount)

    if send_email:
        print("Sending email to:", user["email"])

    return True



#my answer

from typing import Dict,Optional

def is_available(account:Dict[str,int |str ],amount:int)->bool:
    """Return the condition whether user have amount to withdraw"""
    return account["balance"] >= amount

def deduct_amount(account:Dict[str,int |str ],amount:int):    
    """Reduce the withdrawal amount for the account"""
    account["balance"] -= amount
    send_mail()

def send_mail(account:Dict[str,int |str ]):
    """Return mail to the user"""
    return f"Sending mail to {account["name"]}"

def withdraw_amount(account:Dict[str,int |str ],amount:int):
    """perform amount withdraw operation if user have proper balance  """
    if not is_available(account, amount):
        return False
    deduct_amount(account, amount)
      

