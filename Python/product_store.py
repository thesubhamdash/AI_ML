class Product:
    total_products = 0
    
    def __init__(self, name, price):
        self.name = name
        self.price = price
        Product.total_products += 1

    
    def get_info(self):
        print(f"Price of {self.name} is Rs.{self.price}")

    @classmethod
    def get_count(cls):
        print(f"Total Products: {cls.total_products}")

    @staticmethod
    def get_discount(price, percent):
        print(f"Discounted Price is: {price - (price * percent / 100)}") 

p1 = Product("phone", 100000)
p2 = Product("laptop", 250000)
p3 = Product("pen", 100)

p1.get_info()
p2.get_info()
p3.get_info()

p1.get_discount(p1.price, 15)

Product.get_count()
