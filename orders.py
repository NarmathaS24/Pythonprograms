#orders.py
# Define a dictionary to store the current orders
orders = {}

# Define a function to place an order
def place_order(customer_name, item, quantity):
    if customer_name not in orders:
        orders[customer_name] = {}
    if item not in orders[customer_name]:
        orders[customer_name][item] = 0
    orders[customer_name][item] += quantity

# Define a function to print the current orders
def print_orders():
    print("Current orders:")
    for customer_name, customer_orders in orders.items():
        print(f"Customer {customer_name}:")
        for item, quantity in customer_orders.items():
            print(f"- {quantity} x {item}")