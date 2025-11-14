#Question 1
def process_orders(orders):
    total = 0
    valid_orders = []

    for o in orders:
        if o["status"] == "active":
            valid_orders.append(o)

    for vo in valid_orders:
        total += vo["amount"]

    print("Processed", len(valid_orders), "orders")
    return total


#my answer

def calculate_total_amount(active_orders):
    total_amount=0
    """Return total amount of the active order"""
    for order in active_orders:
        total_amount += order["amount"]
    return total_amount

def retrieve_active_orders(orders):
    active_orders=[]
    """Return the list of all the active orders"""
    for order in orders:
        if order["status"] == "active":
            active_orders.append(orders)
    return active_orders


def retrieve_active_orders_amount(orders):

    active_orders=retrieve_active_orders(orders)
    total=calculate_total_amount(active_orders)

    return total
