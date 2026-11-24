orders = []

for i in range(1, 6):
    order = input(f"Enter Order {i}: ")
    orders.append(order)

print("Original Orders:")
print(orders)

additional = input("Enter additional order: ")
orders.append(additional)
print("Updated Orders:")
print(orders)

priority = input("Enter priority order: ")
orders.insert(0, priority)
print("Updated Orders:")
print(orders)

search_order = input("Search for an order: ")
if search_order in orders:
    print(f"Number of Occurrences: {orders.count(search_order)}")
    print(f"First Index: {orders.index(search_order)}")
else:
    print("Can't find order")

cancel_order = input("Enter order to cancel: ")
if cancel_order in orders:
    orders.remove(cancel_order)
    print("Updated Orders:")
    print(orders)
else:
    print("Can't find order")

removed_last = orders.pop()
print(f"Last Order Removed: {removed_last}")

orders.sort()

print("===== FINAL ORDER REPORT =====")
print(f"Orders: {orders}")
print(f"Total Remaining Orders: {len(orders)}")