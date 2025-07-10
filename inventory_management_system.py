inventory = {}

def add_item(item, price, stock):
    if item in inventory:
        print(f"Error: Item '{item}' already exists")
    else:
        inventory[item] = {'price': price, 'stock': stock}
        print(f"Item '{item}' added successfully.")
        

def update_stock(item, quantity):
    if item in inventory:
        new_stock = inventory[item]["stock"] + quantity
        if new_stock < 0:
            print(f"Error: Insufficient stock for '{item}'.")
        else:
            inventory[item]["stock"] = new_stock
            print(f"Stock for '{item}' updated successfully.")
    else:
        print(f"Error: Item '{item}' not found.")

def check_availability(item):
    if item in inventory:
        return inventory[item]["stock"]
    else:
        return "Item not found"
    
def sales_report(sales):
    total_revenue = 0.0
    for item, quentity_sold in sales.items():
        if item not in inventory:
            print(f"Error: Item '{item}' not found.")
            continue
        if inventory[item]["stock"] < quentity_sold:
            print(f"Error: Insufficient stock for '{item}.")
            continue

        inventory[item]["stock"] -= quentity_sold
        revenue = inventory[item]["price"] * quentity_sold
        total_revenue += revenue
    return f"Total revenue: ${total_revenue:.2f}"

add_item("Apple", 0.5, 50)
add_item("Banana", 0.2, 60)
sales = {"Apple": 30, "Banana": 20, "Orange": 10} # Orange should print an error
print(sales_report(sales))
print(inventory)

