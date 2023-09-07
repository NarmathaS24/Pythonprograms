#menu.py
# Define the items available on the menu
menu = {
    'idly': 25,
    'vada': 20,
    'dosa': 40,
    'pongal': 30,
    'coffee': 10,
    'tea': 5
}

# Define a function to print the menu
def print_menu():
    print("Menu:")
    for item, price in menu.items():
        print(f"{item} - Rs. {price}")