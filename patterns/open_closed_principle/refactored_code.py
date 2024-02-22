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

class AndSpecification:
    def __init__(self, *specs):
        self.specs = specs

    def is_satisfied(self, item):
        return all(map(lambda x: x.is_satisfied(item), self.specs))

class Specification:
    def is_satisfied(self, item):
        pass
    
    def __and__(self, other):
        return AndSpecification(self, other)

class Filter:
    def filter_items(self, items, spec):
        for item in items:
            if spec.is_satisfied(item):
                yield item

class ColorSpecification(Specification):
    def __init__(self, color):
        self.color = color

    def is_satisfied(self, item):
        return item.color == self.color

class SizeSpecification(Specification):
    def __init__(self, size):
        self.size = size

    def is_satisfied(self, item):
        return item.size == self.size

red_suitcase = Product("Suitcase", SizeEnum.SMALL,  ColorEnum.RED)
green_suitcase = Product("Suitcase", SizeEnum.MEDIUM, ColorEnum.GREEN)
blue_suitcase = Product("Suitcase", SizeEnum.LARGE,  ColorEnum.BLUE)
blue_toy = Product("Toy", SizeEnum.SMALL,  ColorEnum.BLUE) 

products = [red_suitcase, green_suitcase, blue_suitcase, blue_toy]

blue_color_specification = ColorSpecification(color=ColorEnum.BLUE)
small_size_specification = SizeSpecification(size=SizeEnum.SMALL)

pf = Filter()

blue_products = list(pf.filter_items(products, blue_color_specification))
print("Products filtered by blue color are: ", blue_products)
small_products = list(pf.filter_items(products, small_size_specification))
print("Products filtered by small size are: ", small_products)
small_blue_color_specification = blue_color_specification & small_size_specification
small_blue_products = list(pf.filter_items(products, small_blue_color_specification))
print("Products filtered by small size and blue color are: ", small_blue_products)