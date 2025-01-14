# Step 1: Collect Order Data
orders = []
def add_order(num_orders):
    for i in range(num_orders):
        print(f"\nEnter details for order {i+1}:")
        order_id = input("Order ID: ")
        customer_name = input("Customer Name: ")
        product_name = input("Product Name: ")
        quantity = int(input("Quantity: "))
        price = float(input("Price per unit: "))

        order_data = {
            "order_id": order_id,
            "customer_name": customer_name,
            "product_name": product_name,
            "quantity": quantity,
            "price": price
        }
        orders.append(order_data)



# Step 2: Display All Orders
def display_orders():
    print("\nAll orders:")
    for order in orders:
        print(f"Order ID: {order['order_id']}, Customer Name: {order['customer_name']}, "
              f"Product: {order['product_name']}, Quantity: {order['quantity']}, Price per unit: {order['price']}")

# Step 3: Search for an Order
def search_order(orders, search_order_id):

    #search_order_id = input("\nEnter the order ID to search: ")
    order_found = next((order for order in orders if order["order_id"] == search_order_id), None)

    if order_found:
        print(f"\nOrder found:\nOrder ID: {order_found['order_id']}, Customer Name: {order_found['customer_name']}, "
              f"Product: {order_found['product_name']}, Quantity: {order_found['quantity']}, Price per unit: {order_found['price']}")
    else:
        print("\nOrder not found.")




# Step 4: Update Order Details
def update_order(orders, update_order_id):
    #update_order_id = input("\nEnter the order ID to update: ")
    order_to_update = next((order for order in orders if order["order_id"] == update_order_id), None)

    if order_to_update:
        new_quantity = int(input(f"Enter the new quantity for order {update_order_id}: "))
        new_price = float(input(f"Enter the new price per unit for order {update_order_id}: "))
        order_to_update['quantity'] = new_quantity
        order_to_update['price'] = new_price
        print(f"\nOrder updated:\nOrder ID: {order_to_update['order_id']}, Customer Name: {order_to_update['customer_name']}, "
              f"Product: {order_to_update['product_name']}, Quantity: {order_to_update['quantity']}, Price per unit: {order_to_update['price']}")
    else:
        print("\nOrder not found.")

# Step 5: Calculate Total Cost for Each Order
def calculate_total_cost():
    print("\nTotal cost for each order:")
    for order in orders:
        total_cost = order['quantity'] * order['price']
        print(f"Order ID: {order['order_id']}, Total Cost: {total_cost:.2f}")

# Step 6: Filter Orders by Total Cost Threshold
def filter_orders_by_threshold(orders, threshold):
    threshold = float(input("\nEnter the cost threshold: "))
    print("\nOrders with total cost above threshold:")
    for order in orders:
        total_cost = order['quantity'] * order['price']
        if total_cost > threshold:
            print(f"Order ID: {order['order_id']}, Customer Name: {order['customer_name']}, Total Cost: {total_cost:.2f}")


def main_menu():
    while True:
        print("\n--- Main Menu ---")
        print("1. Add Orders")
        print("2. Display all Orders")
        print("3. Search for an Order")
        print("4. Update an Order")
        print("5. Filter by a Limit")
        print("6. Display all Orders")


        print("7. Exit")




        option = int(input("please select an option"))

        if option == 1:
            num_orders = int(input("Enter the number of orders: "))
            add_order(num_orders)
        if option == 2:
            display_orders()
        if option == 3:
            search_order_id = input("\nEnter the order ID to search: ")
            search_order(orders, search_order_id)
        if option == 4:
            order_id = input("\nEnter the order ID to update: ")
            update_order(orders, order_id)
        if option == 5:
            calculate_total_cost()
        if option == 6:
            threshold = int(input("please set the total cost limit: \n "))
            filter_orders_by_threshold(orders, threshold)
        if option == 7:
            break

if __name__ == "__main__":
    main_menu()