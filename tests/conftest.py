import pytest

from src.Product import Product
from src.Category import Category


@pytest.fixture
def product():
    return Product("AUDI A8", "Объем двигателя 4.0 литра, "
                              "цвет белый, полный привод", 9500000.0, 12)


@pytest.fixture
def category1():
    return Category(
        name="Автомобили",
        description="Автомобили, как средство передвижения",
        products=[
            Product("Mercedes Bens S600", "Объем двигателя 4.0 литра, "
                                          "цвет черный, полный привод",
                    12500000.0, 10),
            Product("BMW X6M", "Объем двигателя 4.4 литра,"
                               " цвет серый, полный привод",
                    10500000.0, 5),
            Product("AUDI A8", "Объем двигателя 4.0 литра, "
                               "цвет белый, полный привод",
                    9500000.0, 12)
        ]
    )


@pytest.fixture
def category2():
    return Category(
        name="Мотоциклы",
        description="Мотоциклы, как средство передвижения",
        products=[
            Product("YAMAHA R1", "Объем двигателя 998 куб.см, "
                                 "цвет синий, задний привод",
                    2890000.0, 14)
        ]
    )
