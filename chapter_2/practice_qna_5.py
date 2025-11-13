def update(data, v):
    for d in data:
        if d["id"] == v:
            d["val"] = 1


from typing import List, Dict
from enum import Enum


class Status(Enum):
    ACTIVE="active"
    INACTIVE="inactive"

def activate_system_status(systems:List[Dict[str,str]],system_id:str):

    """ Activate the given inactive system """

    for system in systems:
        if system["id"]==system_id and system["status"]==Status.INACTIVE:
            system["status"]=Status.ACTIVE