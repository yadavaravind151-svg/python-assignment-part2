# Part 2 - Data Structures Assignment

#About

This is my part 2 assignment submission. i build a Restaurant Menu and Order Management System using python. used only basic data structures like lists, dictionaries and nested dicts. no extra libraries used except copy module for the deepcopy part in task 3.

---

# How to Run

just run the file directly in terminal

```
python part2_order_system.py
```

no need to install anything, copy module is already there in python by default.

---

#Tasks

Task 1 
prints the menu category wise like Starters, Mains, Desserts and shows if item is available or not. also shows total items, how many are available, most expensive item and items below Rs.150.

Task 2 
here i simulated a customer adding items to cart. wrote logic to add item, remove item and update quantity. if someone adds same item twice it wont create duplicate entry it just updates the quantity. also handled cases like item not in menu or item is unavailable. at end it prints the bill with 5% GST added.

Task 3 
used copy.deepcopy() to take backup of inventory before doing anything. then i changed one value manually to show that backup is not affected by changes in original. after that deducted the cart items from inventory. if stock is less than required it prints a warning and deducts only what is available. reorder alerts are printed for items which are at or below reorder level.

Task 4 
calculated total revenue for each day and found best selling day. also found which item appeared in most number of orders. then added new day 2025-01-05 to the sales log and reprinted everything to confirm stats updated. at end printed all orders with numbering using enumerate.

---

# Files

```
part2_order_system.py
README.md
```


