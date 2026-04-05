import copy

# given data - not modifying this

menu = {
    "Paneer Tikka":   {"category": "Starters",  "price": 180.0, "available": True},
    "Chicken Wings":  {"category": "Starters",  "price": 220.0, "available": False},
    "Veg Soup":       {"category": "Starters",  "price": 120.0, "available": True},
    "Butter Chicken": {"category": "Mains",     "price": 320.0, "available": True},
    "Dal Tadka":      {"category": "Mains",     "price": 180.0, "available": True},
    "Veg Biryani":    {"category": "Mains",     "price": 250.0, "available": True},
    "Garlic Naan":    {"category": "Mains",     "price":  40.0, "available": True},
    "Gulab Jamun":    {"category": "Desserts",  "price":  90.0, "available": True},
    "Rasgulla":       {"category": "Desserts",  "price":  80.0, "available": True},
    "Ice Cream":      {"category": "Desserts",  "price": 110.0, "available": False},
}

inventory = {
    "Paneer Tikka":   {"stock": 10, "reorder_level": 3},
    "Chicken Wings":  {"stock":  8, "reorder_level": 2},
    "Veg Soup":       {"stock": 15, "reorder_level": 5},
    "Butter Chicken": {"stock": 12, "reorder_level": 4},
    "Dal Tadka":      {"stock": 20, "reorder_level": 5},
    "Veg Biryani":    {"stock":  6, "reorder_level": 3},
    "Garlic Naan":    {"stock": 30, "reorder_level": 10},
    "Gulab Jamun":    {"stock":  5, "reorder_level": 2},
    "Rasgulla":       {"stock":  4, "reorder_level": 3},
    "Ice Cream":      {"stock":  7, "reorder_level": 4},
}

sales_log = {
    "2025-01-01": [
        {"order_id": 1,  "items": ["Paneer Tikka", "Garlic Naan"],          "total": 220.0},
        {"order_id": 2,  "items": ["Gulab Jamun", "Veg Soup"],              "total": 210.0},
        {"order_id": 3,  "items": ["Butter Chicken", "Garlic Naan"],        "total": 360.0},
    ],
    "2025-01-02": [
        {"order_id": 4,  "items": ["Dal Tadka", "Garlic Naan"],             "total": 220.0},
        {"order_id": 5,  "items": ["Veg Biryani", "Gulab Jamun"],           "total": 340.0},
    ],
    "2025-01-03": [
        {"order_id": 6,  "items": ["Paneer Tikka", "Rasgulla"],             "total": 260.0},
        {"order_id": 7,  "items": ["Butter Chicken", "Veg Biryani"],        "total": 570.0},
        {"order_id": 8,  "items": ["Garlic Naan", "Gulab Jamun"],           "total": 130.0},
    ],
    "2025-01-04": [
        {"order_id": 9,  "items": ["Dal Tadka", "Garlic Naan", "Rasgulla"], "total": 300.0},
        {"order_id": 10, "items": ["Paneer Tikka", "Gulab Jamun"],          "total": 270.0},
    ],
}



# ------------------------------------------------
# TASK 1 - Explore the Menu
# ------------------------------------------------

print("\n===== TASK 1 - Explore the Menu =====\n")

# I need to print items grouped by category
# so first I'll collect all unique categories
categories = []
for item in menu:
    cat = menu[item]["category"]
    if cat not in categories:
        categories.append(cat)

# now print each category and the items under it
for cat in categories:
    print(f"===== {cat} =====")
    for item in menu:
        if menu[item]["category"] == cat:
            if menu[item]["available"] == True:
                status = "[Available]"
            else:
                status = "[Unavailable]"
            print(f"{item}    Rs.{menu[item]['price']:.2f}   {status}")
    print()

# total items on menu
total = len(menu)
print("Total items on menu:", total)

# count available items using a loop
available = 0
for item in menu:
    if menu[item]["available"] == True:
        available += 1
print("Total available items:", available)

# most expensive item - start with first item then compare rest
most_exp = ""
high_price = 0
for item in menu:
    if menu[item]["price"] > high_price:
        high_price = menu[item]["price"]
        most_exp = item
print(f"Most expensive item: {most_exp} - Rs.{high_price:.2f}")

# items under 150
print("Items priced under Rs.150:")
for item in menu:
    if menu[item]["price"] < 150:
        print(f"  {item} - Rs.{menu[item]['price']:.2f}")


# ------------------------------------------------
# TASK 2 - Cart Operations
# ------------------------------------------------

print("\n===== TASK 2 - Cart Operations =====\n")

cart = []

# add item to cart
def add_item(item_name, qty):
    # check if item even exists in menu
    if item_name not in menu:
        print(f"'{item_name}' does not exist in the menu.")
        return

    # check if it's available
    if menu[item_name]["available"] == False:
        print(f"'{item_name}' is not available right now.")
        return

    # check if item is already in cart - if yes just update qty
    for entry in cart:
        if entry["item"] == item_name:
            entry["quantity"] += qty
            print(f"'{item_name}' already in cart. Updated quantity to {entry['quantity']}.")
            return

    # otherwise add as new entry
    cart.append({
        "item": item_name,
        "quantity": qty,
        "price": menu[item_name]["price"]
    })
    print(f"Added '{item_name}' x{qty} to cart.")


# remove item from cart by name
def remove_item(item_name):
    for i in range(len(cart)):
        if cart[i]["item"] == item_name:
            cart.pop(i)
            print(f"Removed '{item_name}' from cart.")
            return
    print(f"'{item_name}' not found in cart.")


# update quantity of an item already in cart
def update_qty(item_name, new_qty):
    for entry in cart:
        if entry["item"] == item_name:
            entry["quantity"] = new_qty
            print(f"Updated '{item_name}' quantity to {new_qty}.")
            return
    print(f"'{item_name}' is not in the cart.")


# show cart
def show_cart():
    print("Current cart:")
    if len(cart) == 0:
        print("  (empty)")
    for entry in cart:
        print(f"  {entry['item']} x{entry['quantity']}  Rs.{entry['quantity'] * entry['price']:.2f}")
    print()


# simulate the steps
add_item("Paneer Tikka", 2)
show_cart()

add_item("Gulab Jamun", 1)
show_cart()

add_item("Paneer Tikka", 1)   # should update qty to 3
show_cart()

add_item("Mystery Burger", 1)  # doesn't exist
show_cart()

add_item("Chicken Wings", 1)   # unavailable
show_cart()

remove_item("Gulab Jamun")
show_cart()

# final order summary
print("========== Order Summary ==========")
subtotal = 0
for entry in cart:
    line = entry["quantity"] * entry["price"]
    subtotal += line
    print(f"{entry['item']}    x{entry['quantity']}    Rs.{line:.2f}")
print("------------------------------------")
gst = subtotal * 0.05
total_pay = subtotal + gst
print(f"Subtotal:         Rs.{subtotal:.2f}")
print(f"GST (5%):         Rs.{gst:.2f}")
print(f"Total Payable:    Rs.{total_pay:.2f}")
print("====================================")





# ------------------------------------------------
# TASK 3 - Inventory Tracker with Deep Copy
# ------------------------------------------------

print("\n===== TASK 3 - Inventory Tracker =====\n")

# deep copy inventory before touching it
inventory_backup = copy.deepcopy(inventory)

# prove deep copy works - change something in inventory and show backup is unchanged
print("Before change - inventory Garlic Naan stock:", inventory["Garlic Naan"]["stock"])
inventory["Garlic Naan"]["stock"] = 999
print("After change  - inventory Garlic Naan stock:", inventory["Garlic Naan"]["stock"])
print("Backup still  - inventory_backup Garlic Naan stock:", inventory_backup["Garlic Naan"]["stock"])
print("Deep copy is working - backup not affected!\n")

# restore back to original before fulfilment
inventory["Garlic Naan"]["stock"] = 30

# now deduct cart items from inventory
print("Deducting cart from inventory:")
for entry in cart:
    name = entry["item"]
    qty = entry["quantity"]
    if inventory[name]["stock"] >= qty:
        inventory[name]["stock"] -= qty
        print(f"  {name}: deducted {qty}, remaining stock = {inventory[name]['stock']}")
    else:
        # not enough stock - deduct whatever is left
        print(f"  Warning: not enough stock for {name}! Only {inventory[name]['stock']} available. Deducting all.")
        inventory[name]["stock"] = 0

# reorder alerts
print("\nReorder Alerts:")
for item in inventory:
    if inventory[item]["stock"] <= inventory[item]["reorder_level"]:
        print(f"  Reorder Alert: {item} - Only {inventory[item]['stock']} unit(s) left (reorder level: {inventory[item]['reorder_level']})")

# print both to confirm they are different
print("\nFinal inventory vs backup:")
for item in inventory:
    print(f"  {item} -> live stock: {inventory[item]['stock']}  | backup stock: {inventory_backup[item]['stock']}")








# ------------------------------------------------
# TASK 4 - Daily Sales Log Analysis
# ------------------------------------------------

print("\n===== TASK 4 - Sales Log Analysis =====\n")

# total revenue per day
print("Revenue per day:")
for date in sales_log:
    total_rev = 0
    for order in sales_log[date]:
        total_rev += order["total"]
    print(f"  {date}: Rs.{total_rev:.2f}")

# best selling day
best_day = ""
best_rev = 0
for date in sales_log:
    day_total = 0
    for order in sales_log[date]:
        day_total += order["total"]
    if day_total > best_rev:
        best_rev = day_total
        best_day = date
print(f"\nBest-selling day: {best_day} with Rs.{best_rev:.2f}")

# most ordered item - count how many orders each item appears in
item_count = {}
for date in sales_log:
    for order in sales_log[date]:
        for item in order["items"]:
            if item not in item_count:
                item_count[item] = 0
            item_count[item] += 1

# find the item with highest count
top_item = ""
top_count = 0
for item in item_count:
    if item_count[item] > top_count:
        top_count = item_count[item]
        top_item = item
print(f"Most ordered item: {top_item} (appeared in {top_count} orders)")

# add new day to sales_log
sales_log["2025-01-05"] = [
    {"order_id": 11, "items": ["Butter Chicken", "Gulab Jamun", "Garlic Naan"], "total": 490.0},
    {"order_id": 12, "items": ["Paneer Tikka", "Rasgulla"],                     "total": 260.0},
]

# reprint after adding new day
print("\nUpdated revenue per day (after adding 2025-01-05):")
best_day2 = ""
best_rev2 = 0
for date in sales_log:
    total_rev = 0
    for order in sales_log[date]:
        total_rev += order["total"]
    print(f"  {date}: Rs.{total_rev:.2f}")
    if total_rev > best_rev2:
        best_rev2 = total_rev
        best_day2 = date
print(f"Best-selling day: {best_day2} with Rs.{best_rev2:.2f}")

# numbered list of all orders using enumerate
print("\nAll orders:")
all_orders = []
for date in sales_log:
    for order in sales_log[date]:
        all_orders.append((date, order))

for i, (date, order) in enumerate(all_orders, 1):
    items_str = ", ".join(order["items"])
    print(f"{i}.  [{date}] Order #{order['order_id']}  - Rs.{order['total']:.2f} - Items: {items_str}")
