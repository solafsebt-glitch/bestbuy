import products
import store


def start(store_obj: store.Store):
    """
    Displays the interactive store menu and handles user choices.
    """
    while True:
        print("\n   Store Menu")
        print("   ----------")
        print("1. List all products in store")
        print("2. Show total amount in store")
        print("3. Make an order")
        print("4. Quit")

        choice = input("Please choose a number: ").strip()

        if choice == "1":
            print("--------------------\nProducts in Store:")
            all_products = store_obj.get_all_products()
            for index, product in enumerate(all_products, start=1):
                print(f"{index}. ", end="")
                product.show()
            print("--------------------")

        elif choice == "2":
            total_qty = store_obj.get_total_quantity()
            print(f"Total of {total_qty} items in store")

        elif choice == "3":
            all_products = store_obj.get_all_products()
            if not all_products:
                print("Sorry, no products available right now.")
                continue

            print("\nAvailable Products:")
            for index, product in enumerate(all_products, start=1):
                print(f"{index}. ", end="")
                product.show()

            shopping_list = []
            print("\nEnter empty product number or finish to complete order.")

            while True:
                prod_num = input("Which product # do you want to buy? (Press enter to finish): ").strip()
                if prod_num == "":
                    break

                try:
                    prod_idx = int(prod_num) - 1
                    if prod_idx < 0 or prod_idx >= len(all_products):
                        print("Invalid product number. Try again.")
                        continue

                    qty_str = input("What amount do you want? ").strip()
                    qty = int(qty_str)
                    if qty <= 0:
                        print("Quantity must be greater than zero.")
                        continue

                    selected_product = all_products[prod_idx]
                    shopping_list.append((selected_product, qty))
                    print("Product added to list!")
                except ValueError:
                    print("Please enter valid numbers.")

            if shopping_list:
                try:
                    total_price = store_obj.order(shopping_list)
                    print(f"*********\nOrder made! Total payment: ${total_price}\n*********")
                except Exception as e:
                    print(f"Error placing order: {e}")
            else:
                print("No products were ordered.")

        elif choice == "4":
            print("Thank you for shopping with Best Buy! Goodbye.")
            break
        else:
            print("Invalid choice, please choose a number between 1 and 4.")


if __name__ == "__main__":
    # Setup initial stock of inventory
    product_list = [
        products.Product("MacBook Air M2", price=1450, quantity=100),
        products.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
        products.Product("Google Pixel 7", price=500, quantity=250)
    ]
    best_buy = store.Store(product_list)

    # Start the user interface menu
    start(best_buy)