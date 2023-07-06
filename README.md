
# Tasty Bites - Food Delivery System

Tasty Bites is a command-line food delivery system that allows users to manage a menu, place orders, and review order details. The system provides features such as adding/removing dishes, updating dish availability, taking new orders, updating order status, and reviewing all orders.


## Installation

1. Clone the repository to your local machine:
   ```
   git clone https://github.com/DishaGup/tasty-dishes-find.git
   ```

2. Make sure you have Python installed (version 3.6 or above). You can download Python from the official website: [Python Downloads](https://www.python.org/downloads/)

3. Install the required dependencies by running the following command in your terminal or command prompt:
   ```
   pip install -r requirements.txt
   ```

## Usage

1. Open a terminal or command prompt and navigate to the project directory.

2. Run the following command to start the program:
   ```
   python zomato.py
   ```

3. Follow the on-screen instructions to interact with the system. The program will display a menu of options:

   - **Add a new dish to the menu**: Choose this option (Press 1 key )  to add a new dish to the menu. Enter the dish ID, name, and price when prompted.

   - **Remove a dish from the menu**: Choose this option (Press 2 key )  to remove a dish from the menu. Enter the dish ID when prompted.

   - **Update the availability of a dish**: Choose this option (Press 3 key )  to update the availability of a dish. Enter the dish ID and availability (True/False) when prompted.

   - **Take a new order**: Choose this option (Press 4 key )  to take a new order. Enter the customer's name and the dish IDs (separated by commas) when prompted.

   - **Update the status of an order**: Choose this option (Press 5 key )  to update the status of an order. Enter the order ID and the new status when prompted.

   - **Review all orders**: Choose this option (Press 6 key )  to review all orders placed. The program will display the order ID, customer name, ordered dishes, status, and total price for each order.

   - **Display the menu**: Choose this option (Press 7 key )  to view the current menu. The program will display the ID, name, and price of each dish.

   - **View item details**: Choose this option (Press 8 key )  to view the details of a specific dish. Enter the dish ID when prompted.

   - **View orders by status**: Choose this option  (Press 9 key )  to view orders filtered by status. Enter the desired status (e.g., 'ready for pickup') when prompted.

   - **Exit**: Choose this option (Press 0 key )  to exit the program.

4. To exit the program, select the "Exit" option from the menu.

## Data Persistence

The system automatically saves the menu and order data to a file named `data.json`. This ensures that the data is persisted across multiple usages of the system. The data is loaded at the start of the program and saved before exiting.

## Extra Adventures

The project includes extra features that you can explore:

- **Price Calculation**: The system calculates and displays the total price of each order based on the price of each ordered dish.

- **Status Filter**: Add an option to view only the orders with a specific status. This allows for easy tracking of orders in different stages, such as 'ready for pickup' or 'delivered'.

- **Data Persistence**: The menu and order data are saved to a file, allowing data to persist across multiple usages of the system. This ensures that the culinary journey and order history are maintained even after restarting the program.

## Contributing

Contributions are welcome! If
you have any suggestions, improvements, or bug fixes, feel free to open an issue or submit a pull request. 


---

### Enjoy your culinary journey with Zesty Zomato!


