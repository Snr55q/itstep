class Product:
    def __init__(self):
        self.name = "Blasted"
        self.price = 1300
    def printer(self):
        print(self.name)
        print(self.price)

product1 = Product()
product1.printer()