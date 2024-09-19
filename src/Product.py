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


# product1 = Product("Mercedes Bens S600", "Объем двигателя 4.0 литра, цвет черный, полный привод", 12500000.0, 10)
# product2 = Product("BMW X6M", "Объем двигателя 4.4 литра, цвет серый, полный привод", 10500000.0, 5)
# product3 = Product("AUDI A8", "Объем двигателя 4.0 литра, цвет белый, полный привод", 9500000.0, 12)
