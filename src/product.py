from src.base_product import BaseProduct
from src.print_mixin import PrintMixin


class Product(BaseProduct, PrintMixin):
    """
Для класса Product определен следующие свойства:
название (name),
описание (description),
цена (price),
количество в наличии (quantity).
    """
    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity
        super().__init__()

    def __str__(self):
        return f'{self.name}, {self.__price}. Остаток: {self.quantity}'

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, number):
        if number <= 0:
            print("Цена не должна быть нулевая или отрицательная")
        else:
            self.__price = number

    @classmethod
    def new_product(cls, product_dict: dict):
        name, description, price, quantity = product_dict.values()
        return cls(name, description, price, quantity)

    def __add__(self, other):
        if type(other) is self.__class__:
            return self.quantity * self.__price + other.quantity * other.__price
        raise TypeError


product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
