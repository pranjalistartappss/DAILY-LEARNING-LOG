class Product:

    def __init__(self, name, price):
        self.__name = name
        self.__price = price

    def get_price(self):
        return self.__price

    def set_price(self, price):
        if price > 0:
            self.__price = price
        else:
            print("Invalid Price")

    def show_details(self):
        print("Product Name :", self.__name)
        print("Price :", self.__price)


product = Product("Laptop", 50000)
product.show_details()
product.set_price(55000)
print()
product.show_details()