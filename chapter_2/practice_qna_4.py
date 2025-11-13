#4.Question

def account(account_list):
    account = 0
    for acc in account_list:
        account += acc["amount"]
    return account

#myanswer

from typing import List,Dict,Optional

def calculate_total_amount_of_accounts(accounts: List[Dict[str,int]])->Optional[int]:
    

    if not accounts:
        return None
    
    total_amount = 0
    """Calculate total amount of the accounts"""
    for account in accounts:
        total_amount+=account["amount"]
    return total_amount    


#Refactor

from typing import List, Dict, Optional

def calculate_total_amount_for_accounts(accounts: List[Dict[str, int]]) -> Optional[int]:
    """Return the total amount for all accounts, or None if the list is empty."""
    if not accounts:
        return None
    
    total_amount = 0
    for account in accounts:
        total_amount += account["amount"]
    return total_amount
