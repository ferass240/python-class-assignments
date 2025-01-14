my_orders = []
def addOrder(number_of_orders):
    
    for i in range(number_of_orders):
        print (f"Enter details for order {i+1}") 
        id = int(input("Please Enter Order ID: \n"))
        customer_name = input("Please Enter Customer Name: \n")
        prod_name = input("Please Enter Product Name : \n")
        quantity = int(input("Please Enter Quantity: \n"))
        ppu = int(input("Please Enter The Price Per Unit: \n"))
        order = dict(id = "id", Customer_name = "customer_name",prod_name = "prod_name",
                quantity = "quantity"   ,ppu = "ppu")
        my_orders.add(order)


number_of_orders = int(input("Please Enter The Number Of Orders: \n"))

addOrder(number_of_orders)
print(my_orders)