class  Rectangle:
    def __init__(self):
        self.width = 20
        self.height = 10
    def calculate_area (self):
        print(self.width * self.height)
    def calculate_perimeter(self):
        print(self.width + self.height)

rectangle = Rectangle()
rectangle.calculate_area()
rectangle.calculate_perimeter()
