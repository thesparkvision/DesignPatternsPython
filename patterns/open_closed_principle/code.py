from enum import Enum

class SizeEnum(Enum):
    SMALL = "small"
    MEDIUM = "medium"
    LARGE = "large"

class ColorEnum(Enum):
    BLUE = "blue"
    GREEN = "green"
    RED = "red"

class Product:
    def __init__(self, name, size, color):
        self.name = name
        self.size = size
        self.color = color

    def __str__(self):
        return f"{self.size.value}-{self.color.value} {self.name}"

    def __repr__(self):
        return f"{self.size.value}-{self.color.value} {self.name}"

class ProductFilter:
    def filter_by_color(self, products, color):
        for product in products:
            if product.color == color:
                yield product
    
    def filter_by_size(self, products, size):
         for product in products:
            if product.size == size:
                yield product

    def filter_by_size_and_color(self, products, size, color):
         for product in products:
            if product.size == size and product.color == color:
                yield product

red_suitcase = Product("Suitcase", SizeEnum.SMALL,  ColorEnum.RED)
green_suitcase = Product("Suitcase", SizeEnum.MEDIUM, ColorEnum.GREEN)
blue_suitcase = Product("Suitcase", SizeEnum.LARGE,  ColorEnum.BLUE)
blue_toy = Product("Toy", SizeEnum.SMALL,  ColorEnum.BLUE) 

products = [red_suitcase, green_suitcase, blue_suitcase, blue_toy]

pf = ProductFilter()
blue_products = list(pf.filter_by_color(products=products, color=ColorEnum.BLUE))
print("Products filtered by blue color are: ", blue_products)
small_products = list(pf.filter_by_size(products=products, size=SizeEnum.SMALL))
print("Products filtered by small size are: ", small_products)
small_blue_products = list(pf.filter_by_size_and_color(products=products, size=SizeEnum.SMALL, color=ColorEnum.BLUE))
print("Products filtered by small size and blue color are: ", small_blue_products)