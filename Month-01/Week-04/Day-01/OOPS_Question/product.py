class Product:
    def __init__(self, product_id, product_name, category, brand, price, stock, rating, warranty):
        self.product_id = product_id
        self.product_name = product_name
        self.category = category
        self.brand = brand
        self.price = price
        self.stock = stock
        self.rating = rating
        self.warranty = warranty

    def buy(self):
        print(self.product_name, "purchased successfully.")

    def add_to_cart(self):
        print(self.product_name, "added to cart.")

    def update_stock(self):
        self.stock = self.stock + 10
        print("Stock Updated.")

    def apply_discount(self):
        self.price = self.price - 1000
        print("Discount Applied.")

    def show_details(self):
        print("Product Details")
        print("Product ID:", self.product_id)
        print("Product Name:", self.product_name)
        print("Category:", self.category)
        print("Brand:", self.brand)
        print("Price:", self.price)
        print("Stock:", self.stock)
        print("Rating:", self.rating)
        print("Warranty:", self.warranty)

product1 = Product(101,"Laptop","Electronics","HP",60000,20,4.5,"2 Years")

product1.show_details()
product1.add_to_cart()
product1.buy()
product1.update_stock()
product1.apply_discount()
product1.show_details()