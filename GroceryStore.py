product_catalog = {
    "Apple": [100, 10],
    "Banana": [60, 20],
    "Milk": [150, 5]
}


def display_products():
    print("\nAvailable Products:")
    for item, details in product_catalog.items():
        price, stock = details
        print(f"{item} - Rs.{price}, In stock: {stock}")

        if stock < 5:
            print("Low stock alert!")


def add_update_product():
    name = input("Enter product name: ")
    price = int(input("Enter price: "))
    stock = int(input("Enter stock: "))

    product_catalog[name] = [price, stock]
    print("Product added/updated successfully!")


def purchase_item():
    total_bill = 0

    while True:
        item = input("Enter item to purchase (or 'done' to finish): ")

        if item.lower() == "done":
            break

        if item not in product_catalog:
            print("Item not found")
            continue

        quantity = int(input("Enter quantity: "))
        price, stock = product_catalog[item]

        if quantity > stock:
            print("Not enough stock")
            continue

        cost = price * quantity
        total_bill += cost
        product_catalog[item][1] -= quantity

        print(f"{item} added. Cost: Rs.{cost}")

    print("\nTotal Bill: Rs.", total_bill)


while True:
    print("\nWelcome to Smart Grocery Store Assistant")
    print("1. View Products")
    print("2. Add/Update Product")
    print("3. Purchase Items")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        display_products()
    elif choice == "2":
        add_update_product()
    elif choice == "3":
        purchase_item()
    elif choice == "4":
        print("Thank you for visiting!")
        break
    else:
        print("Invalid choice")
