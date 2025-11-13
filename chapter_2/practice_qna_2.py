def getData(u, lst):
    res = []
    for x in lst:
        if x['n'] == u:
            res.append(x)
    return res


#myanswer

def get_users_by_name(user_name, users):

    results=[]

    for user in users:

        if user["n"]==user_name:
            results.append(user)
    return results

#refactor

from typing import List, Dict

def filter_users_by_name(user_name: str, users: List[Dict[str, str]]) -> List[Dict[str, str]]:
    """Return a list of users whose name matches the given user_name."""
    results = []
    for user in users:
        if user["name"] == user_name:
            results.append(user)
    return results
