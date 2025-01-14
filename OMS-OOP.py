class Order:
    def __init__(self, order_id, customer_name, products):
        self.oder_id = order_id
        self.customer_name = customer_name
        self.products = products

    def display_order(self):
        total_cost = self.calculate_total()
        print(f"Oder_ID: {self.oder_id}\nCustomer Name: {self.customer_name}\nProducts: {self.products}\t{total_cost:.2f}")

    def calculate_total(self):
        total_cost = 0
        for prod in self.products:
            total_cost = total_cost + prod[2] * prod[1]

        return total_cost

    def update_quantity(self, product_name, new_quantity):
        for prod in self.products:
            if prod[0] == product_name:
                prod[1] = new_quantity
            else:
                print("No such product found!")


class OrderManager:

    def __init__(self):
        self.list_orders = []


    def add_order(self, order):
        self.list_orders.append(order)
        print(f"Order {order.oder_id} added.")


    def display_all_orders(self):
        for order in self.list_orders:
            order.display_order()


    def search_order(self, order_id):

        for order in self.list_orders:
            if order.oder_id == order_id:
                order.display_order()

    def list_orders_above_threshold(self, threshold):
        print(f"Orders with total cost above {threshold:.2f}:")
        for order in self.list_orders:
            if order.calculate_total() > threshold:
                order.display_order()



# Main program

def main():
    manager = OrderManager()

    while True:
        print("\n1. Add order\n2. Display all orders\n3. Search for order\n"
              "4. Update product quantity\n5. Calculate total cost of each order\n"
              "6. List orders above a certain total cost\n7. Exit")



