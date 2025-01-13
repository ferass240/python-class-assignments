
my_customers = []
#number_of_customers = int(input("Please Enter The Number of Customers: \n"))


def addCustomers(number_of_customers):
    for i in range(number_of_customers):
        print (f"Enter details for Customer {i+1}") 
        customer_name = input("Please Enter Customer Name: \n")
        email = input("Please Enter E-mail : \n")
        phone = int(input("Please Enter Costumer Phone-number: \n"))
        purchases_str = input(f"Please Enter {customer_name}'s purchases (comma-separated): \n")
        result = purchases_str.split(",")
        result = map(float, result)
        purchases = tuple(result)  


        customer = dict(customer_name = customer_name, email = email,
                phone = phone, purchases = purchases)
        my_customers.append(customer)


#display details 

 

def diplayCustomers():
    print("\n All Customers Details")

    for cus in my_customers:
        print(f"Name: {cus["customer_name"]}\tE-mail: {cus["email"]}\t \
            Phone-Number: {cus["phone"]}\tPurchase History:  {cus["purchases"]}")
        
def search_customer(search):
    #search = input("Please Input customer's name: \n")

    customer_found = next( (cus for cus in my_customers if cus["customer_name"] == search),\
                        None)

    if customer_found:
        print(f"Name: {customer_found["customer_name"]}\tE-mail: {customer_found["email"]}\tPhone-Number:\
        {customer_found["phone"]}\tPurchase History:  {customer_found["purchases"]}")
    else: 
        print(f"{search} was not found among customers")


def update_phone_number(cus_name, cus_new_phone):
    #phone_cus = input("Please Input customer's name and new phone number (comma- separated ):")

    #update = phone_cus.split(",")

    #cus_name = update[0]
    #cus_new_phone = update[1]
    customer_found = next( (cus for cus in my_customers if cus["customer_name"] == cus_name),None)
    if customer_found:
        customer_found["phone"] = cus_new_phone
        print(f"Name: {customer_found["customer_name"]}\tE-mail: {customer_found["email"]}\tPhone-Number:\
        {customer_found["phone"]}\tPurchase History:  {customer_found["purchases"]}")
    else: 
        print(f"{cus_name} was not found among customers") 




def filter_by_number_of_purchases(numer_of_purchases):
    customer_found = next( (cus for cus in my_customers if len(cus["purchases"]) > numer_of_purchases),None)
    if customer_found is None:
        print(f"no customer has over {numer_of_purchases} purchases")
    else: 
        print(f"\n Customers with over {numer_of_purchases} purchases:")
    for cus in my_customers:
        if len(cus["purchases"]) > numer_of_purchases:
            print(f"Name: {cus["customer_name"]}\tE-mail: {cus["email"]}\tPhone-Number:\
            {cus["phone"]}\tPurchase History:  {cus["purchases"]}")

def filter_customers_by_threshold(threshold):
    #threshold = int(input("Please Enter Purchases Threshold:\n"))

    customer_found = next((cus for cus in my_customers if  sum(cus["purchases"]) > threshold ), None)
    if customer_found is None: 
        print(f"No Customer exceeded the {threshold} limit")  
    else: 
        print(f"\n Customers exceeded {threshold} limit: ")
    for cus in my_customers:
        if sum(cus["purchases"]) > threshold:
            print(f"Name: {cus["customer_name"]}\tE-mail: {cus["email"]}\tPhone-Number:\
            {cus["phone"]}\tPurchase History:  {cus["purchases"]}, total purchases cost:{sum(cus["purchases"])} ")


while True:

    option = int(input("select an option: \n"))
    if option < 1 or option > 7:
        print("This option is not available!")
        pass

    if option ==  1:
        number_of_customers = int(input("Please Enter The Number of Customers: \n"))
        addCustomers(number_of_customers)
    if option == 2:
        diplayCustomers()
    if option == 3:
        search = input("Please Input customer's name: \n")
        search_customer(search)
    if option == 4:
        phone_cus = input("Please Enter customer's name and new phone number (comma- separated ):")
        update = phone_cus.split(",")
        cus_name = update[0]
        cus_new_phone = update[1]
        update_phone_number(cus_name, cus_new_phone)
    if option == 5:
        numer_of_purchases = int(input("Please Enter number of Purchases: \n"))
        filter_by_number_of_purchases(numer_of_purchases)

    if option == 6:
        threshold = int(input("Please Enter Purchases Threshold:\n"))
        filter_customers_by_threshold(threshold)
    if option == 7:
        break