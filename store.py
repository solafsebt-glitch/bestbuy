from typing import List, Tuple
import products


class Store:
    def __init__(self, product_list: List[products.Product] = None):
        if product_list is None:
            self.products = []
        else:
            self.products = product_list

    def add_product(self, product: products.Product):
        """Adds a product to the store."""
        self.products.append(product)

    def remove_product(self, product: products.Product):
        """Removes a product from the store if it exists."""
        if product in self.products:
            self.products.remove(product)

    def get_total_quantity(self) -> int:
        """Returns the total quantity of all items in the store."""
        total = 0
        for product in self.products:
            total += product.get_quantity()
        return total

    def get_all_products(self) -> List[products.Product]:
        """Returns a list of all active products in the store."""
        active_products = []
        for product in self.products:
            if product.is_active():
                active_products.append(product)
        return active_products

    def order(self, shopping_list: List[Tuple[products.Product, int]]) -> float:
        """
        Buys products based on a shopping list (list of tuples: Product, quantity)
        and returns the total price of the order.
        """
        total_order_price = 0.0
        for product, quantity in shopping_list:
            # Call the buy method of the Product class, which handles stock and active checks
            total_order_price += product.buy(quantity)
        return total_order_price


# Testing block
if __name__ == "__main__":
    product_list = [
        products.Product("MacBook Air M2", price=1450, quantity=100),
        products.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
        products.Product("Google Pixel 7", price=500, quantity=250),
    ]

    best_buy = Store(product_list)
    active_products = best_buy.get_all_products()
    print("Total quantity in store:", best_buy.get_total_quantity())

    # Order products and print total price
    order_price = best_buy.order([(active_products[0], 1), (active_products[1], 2)])
    print(f"Order cost: {order_price} dollars.")