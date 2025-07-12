customer_id = input("Enter customer ID: ")
service_name = input("Enter the service_name: ")
supplier_name = input("Enter the supplier_name: ")
supplier_contact_number = int(input("Enter the supplier_contact_number: "))
location = input("Enter location: ")
service_cost = float(input("Enter the service_cost: "))  
service_description = input("Enter the description: ")
service_rating = float(input("Enter rating: "))

avail_input = input("Is the service available? (yes/no): ")
service_availability = avail_input.lower() == "yes"

service_feedback = input("Enter your feedback: ")
categories = list(input("Enter categories (comma-separated): ").split(","))
service_tags = tuple(input("Enter service tags (comma-separated): ").split(","))
cashback = float(input("Enter the cashback (%): "))
price = float(input("Enter the price (₹): "))

product_features = set(["Free", "Instant", "Cashback"])
supplier_input = input("Enter supplier details in format name,contact,location: ").split(",")
supplier_details = {
    "name": supplier_input[0],
    "contact": supplier_input[1],
    "location": supplier_input[2]
}
stock_details = set(input("Enter stock details (comma-separated): ").split(","))

# Printing values
#camma-separated output
print(customer_id, service_name, price, sep=',')
#percentage output
print("cashback: %.2f%%" % cashback)
print("service_rating: %.1f" % service_rating)
#f string output
print(f"Price: {price:.2f}")
#formatted output
print("service_tags: {}".format(service_tags))
print("Supplier: {}, Contact: {}, Location: {}".format(
    supplier_details["name"],
    supplier_details["contact"],
    supplier_details["location"]
))
