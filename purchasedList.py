from product import Product

class ProductList():
    def __init__(self,name):
        self.name = name
        self.product_list = []

    def add_product(self, product):
        self.product_list.append(product)

    def get_the_purchased_product(self):
        total_cost = float(0.0)
        for m in self.product_list:
            total_cost += m.price
        print("This is the total cost of the product: ", total_cost)
