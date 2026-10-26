"""A simple Online Food Ordering System."""


MENU = {
    1: {"name": "Margherita Pizza", "price": 199},
    2: {"name": "Veg Burger", "price": 99},
    3: {"name": "Paneer Wrap", "price": 149},
    4: {"name": "French Fries", "price": 89},
    5: {"name": "Cold Coffee", "price": 119},
}


def display_menu():
    """Return all available food items."""
    return MENU.copy()


def add_to_cart(cart, item_id, quantity=1):
    """Add an item to the cart."""
    if item_id not in MENU:
        raise ValueError("Invalid menu item.")

    if not isinstance(quantity, int) or isinstance(quantity, bool) or quantity <= 0:
        raise ValueError("Quantity must be a positive integer.")

    cart[item_id] = cart.get(item_id, 0) + quantity
    return cart


def calculate_total(cart):
    """Calculate the total price of items in the cart."""
    total = 0

    for item_id, quantity in cart.items():
        if item_id not in MENU:
            raise ValueError("Invalid menu item.")

        if not isinstance(quantity, int) or isinstance(quantity, bool) or quantity <= 0:
            raise ValueError("Quantity must be a positive integer.")

        total += MENU[item_id]["price"] * quantity

    return total


def place_order(cart, customer_name):
    """Validate and create an order summary."""
    if not isinstance(customer_name, str) or not customer_name.strip():
        raise ValueError("Customer name is required.")

    if not cart:
        raise ValueError("Cannot place an empty order.")

    return {
        "customer": customer_name.strip(),
        "items": cart.copy(),
        "total": calculate_total(cart),
        "status": "Order Placed",
    }


if __name__ == "__main__":
    print("=== Online Food Ordering System ===")
    print("\nAvailable Menu:")

    for item_id, item in display_menu().items():
        print(f"{item_id}. {item['name']} - Rs. {item['price']}")

    cart = {}

    try:
        item_id = int(input("\nEnter the item number: "))
        quantity = int(input("Enter quantity: "))
        customer = input("Enter customer name: ")

        add_to_cart(cart, item_id, quantity)
        order = place_order(cart, customer)

        print("\nOrder Confirmation")
        print(f"Customer: {order['customer']}")
        print(f"Total: Rs. {order['total']}")
        print(f"Status: {order['status']}")

    except ValueError as error:
        print(f"Error: {error}")
