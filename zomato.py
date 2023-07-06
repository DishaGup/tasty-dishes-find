import json

# Save data to a file


def save_data(menu, orders):
    data = {
        "menu": menu,
        "orders": orders
    }
    with open("data.json", "w") as file:
        json.dump(data, file)

# Load data from a file


def load_data():
    try:
        with open("data.json", "r") as file:
            data = json.load(file)
            menu = data.get("menu", [])
            orders = data.get("orders", [])
            return menu, orders
    except FileNotFoundError:
        return [], []

# Main program


# Load data from the file
menu, orders = load_data()


def display_menu(menu):
    print("Menu:")
    for dish in menu:
        print(f"{dish['id']}. {dish['name']} - ${dish['price']}")
        print("-----------")
    print()


def add_dish(menu, dish_id, dish_name, price):
    for dish in menu:
        if dish["id"] == dish_id:
            print("Dish with the same ID already exists.")
            return

    dish = {"id": dish_id, "name": dish_name,
            "price": price, "availability": True}
    menu.append(dish)
    print("Dish added successfully.")

# Usage example
# add_dish(menu, 4, "Paneer Tikka", 9.99)


def remove_dish(menu, dish_id):
    for dish in menu:
        if dish["id"] == dish_id:
            menu.remove(dish)
            print("Dish removed Successfully")
            return
    print("Dish not Found")


# remove_dish(menu, 2)


def update_availability(menu, dish_id, availability):
    for dish in menu:
        if dish["id"] == dish_id:
            dish["availability"] = availability
            print("Availability updated successfully.")
            return

    print("Dish not found.")

# Usage example
# update_availability(menu, 1, False)


def take_order(menu, customer_name, dish_ids):
    order_id = len(orders) + 1  # Generate a unique order ID

    order = {
        "id": order_id,
        "customer_name": customer_name,
        "dishes": [],
        "status": "received"
    }

    for dish_id in dish_ids:
        dish_id = int(dish_id)  # Convert dish_id to integer
        dish = find_dish_by_id(menu, dish_id)

        if dish:
            if dish["availability"]:
                order["dishes"].append(dish)
                print(f"Dish with ID {dish_id} added to the order.")
            else:
                print(f"Dish with ID {dish_id} is not available.")
        else:
            print(f"Dish with ID {dish_id} not found in the menu.")
            return

    # Process the order further (e.g., update status, calculate total, etc.)
    orders.append(order)
    print("Order placed successfully.")
    print("-----------")


# Helper function to find a dish by ID


def find_dish_by_id(menu, dish_id):
    for dish in menu:
        if dish["id"] == dish_id:
            return dish
    return None

# Usage example
# take_order(menu, "John Doe", [1, 3])


def update_order_status(orders, order_id, status):
    for order in orders:
        if order["id"] == order_id:
            order["status"] = status
            print("Order status updated successfully.")
            print("-----------")
            return

    print("Order not found.")
    print("-----------")


# Usage example
# update_order_status(orders, 1, "preparing")


def review_orders(orders):
    if len(orders) == 0:
        print("No orders found.")
        return

    print("Reviewing all orders:")
    for order in orders:
        print(f"Order ID: {order['id']}")
        print(f"Customer Name: {order['customer_name']}")
        print("Dishes:")
        total_price = 0.0  # Initialize total price for the order
        for dish in order['dishes']:
            print(f"- {dish['name']} - ${dish['price']}")
            total_price += dish['price']  # Add dish price to the total price
        print(f"Status: {order['status']}")
        # Display the total price with two decimal places
        print(f"Total Price: ${total_price:.2f}")
        print("-----------------------")


# Usage example
# review_orders(orders)


def update_order_status(menu, orders, order_id, status):
    for order in orders:
        if order["id"] == order_id:
            order["status"] = status
            print("Order status updated successfully.")
            return

    print("Order not found.")

# Usage example
# update_order_status(orders, 1, "preparing")


# Main program

while True:
    print("Zesty Zomato - Food Delivery System")
    print("1. Add a new dish to the menu")
    print("2. Remove a dish from the menu")
    print("3. Update the availability of a dish")
    print("4. Take a new order")
    print("5. Update the status of an order")
    print("6. Review all orders")
    print("7. Display the menu")
    print("8. View item details")
    print("9. View orders by status")
    print("0. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        dish_id = int(input("Enter dish ID: "))
        dish_name = input("Enter dish name: ")
        price = float(input("Enter dish price: "))

        add_dish(menu, dish_id, dish_name, price)

    elif choice == "2":
        dish_id = int(input("Enter dish ID: "))

        remove_dish(menu, dish_id)

    elif choice == "3":
        dish_id = int(input("Enter dish ID: "))
        availability = input(
            "Enter availability (True/False): ").lower() == "true"

        update_availability(menu, dish_id, availability)

    elif choice == "4":
        customer_name = input("Enter Your name: ")
        display_menu(menu)
        dish_ids = input("Enter dish Ids (comma-separated): ").split(",")
        take_order(menu, customer_name, dish_ids)

    elif choice == "5":
        review_orders(orders)
        order_id = input("Enter Unique Order Id: ")
        status = input("Enter Order status: ")
        update_order_status(menu, orders, order_id, status)

    elif choice == "6":
        review_orders(orders)

    elif choice == "7":
        display_menu(menu)

    elif choice == "8":
        dish_id = int(input("Enter dish ID: "))
        dish = find_dish_by_id(menu, dish_id)
        if dish:
            print("Item details:")
            print(f"ID: {dish['id']}")
            print(f"Name: {dish['name']}")
            print(f"Price: ${dish['price']}")
            print(
                f"Availability: {'Available' if dish['availability'] else 'Not available'}")

    elif choice == "9":
        status = input("Enter the status to filter orders: ")
        filtered_orders = [
            order for order in orders if order['status'].lower() == status.lower()]
        review_orders(filtered_orders)

    elif choice == "0":
        save_data(menu, orders)
        break

    else:
        print("Invalid choice. Please try again.")
