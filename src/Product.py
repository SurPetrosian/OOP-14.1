class Product:
    """
   Для класса Product определен следующие свойства:
название (name),
описание (description),
цена (price),
количество в наличии (quantity).
    """
    name: str  # название
    description: str  # описание
    price: float  # цена
    quantity: int  # кол-во в наличии

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity
