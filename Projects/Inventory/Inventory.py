start_inventory = 20

num_items = start_inventory

while num_items > 0:
    print("We have " + str(num_items) + " items in inventory.")
    user_purchase = input("How many would you like to buy? ")
    if int(user_purchase) > num_items:
        print("Not Enough Stock")
    else:
        num_items = num_items - int(user_purchase)
print("All out!")