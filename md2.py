import canteen.menu as menu
import canteen.orders as orders
import canteen.customers as customers
# Print the menu
menu.print_menu()
# Create some customers
alice = customers.Customer("Narmatha", "9566388346", "123 Coimbatore")
bob = customers.Customer("Jerome", "9811234561", "456 chennai")
# Place some orders
orders.place_order(alice.get_phone(), 'idly', 2)
orders.place_order(alice.get_phone(), 'dosa', 1)
orders.place_order(bob.get_phone(), 'vada', 3)
orders.place_order(bob.get_phone(), 'coffee', 1)
# Print the current orders
orders.print_orders()
