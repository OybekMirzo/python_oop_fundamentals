Problem 3 (Medium): Shopping Cart System
Create a ShoppingCart class that manages a collection of items for an online store.

Requirements:

1. Define a class ShoppingCart with these class variables:
store_name = “Online Bazaar”
tax_rate = 0.08 (8% tax)

2. Define __init__ with parameter customer_name:
Store as instance variable: self.customer_name
Initialize self.items as an empty list to hold cart items
Each item in the list should be a dictionary with keys: "name" and "price"

3. Create a method add_item(self, item_name, price):
Append a dictionary {"name": item_name, "price": price} to self.items
Print: "Added {item_name} (${price}) to cart"
If price <= 0, print: "Invalid price. Must be greater than 0" and do not add the item

4. Create a method remove_item(self, item_name):
Find and remove the first item with matching name from self.items
Print: "Removed {item_name} from cart" if found
Print: "Item '{item_name}' not found in cart" if not found

5. Create a method get_subtotal(self) that returns the sum of all item prices

6. Create a method get_total(self) that returns subtotal + (subtotal × tax_rate)

7. Create a method display_cart(self) that prints:
"Cart for {customer_name} at {store_name}:"
Then each item on a new line: " - {item_name}: ${price}"
Then: "Subtotal: ${subtotal}"
Then: "Total (with tax): ${total}"

8. Test with:
Cart for “Dilshod”
Add: “Laptop” ($999.99), “Mouse” ($25.50), “Keyboard” ($75.00)
Remove: “Mouse”
Display cart
Print subtotal and total separately

Input
```
Customer: "Dilshod"
Items to add:
- "Laptop", 999.99
- "Mouse", 25.50
- "Keyboard", 75.00
Item to remove: "Mouse"
```
Expected Output
```
Added Laptop ($999.99) to cart
Added Mouse ($25.5) to cart
Added Keyboard ($75.0) to cart
Removed Mouse from cart
Cart for Dilshod at Online Bazaar:
  - Laptop: $999.99
  - Keyboard: $75.0
Subtotal: $1074.99
Total (with tax): $1160.9892
1074.99
1160.9892
```