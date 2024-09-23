class Product:
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
