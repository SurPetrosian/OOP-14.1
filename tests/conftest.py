import pytest

from src.lawngrass_product import LawnGrass
from src.product import Product
from src.smartphone_product import Smartphone
from src.сategory import Category


@pytest.fixture
def product():
    return Product("AUDI A8", "Объем двигателя 4.0 литра, "
                              "цвет белый, полный привод", 9500000.0, 12)


@pytest.fixture()
def product1():
    return Product("BMW X6M", "Объем двигателя 4.4 литра,"
                              " цвет серый, полный привод",
                   10500000.0, 5)


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


@pytest.fixture
def category3():
    return Category(
        name="Мотоциклы",
        description="Мотоциклы, как средство передвижения",
        products=[]
    )


@pytest.fixture
def smartphone_product1():
    return Smartphone("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5, 95.5,
                      "S23 Ultra", 256, "Серый")


@pytest.fixture
def smartphone_product2():
    return Smartphone("Iphone 15", "512GB, Gray space", 210000.0, 8, 98.2, "15", 512, "Gray space")


@pytest.fixture
def lawngrass_product1():
    return LawnGrass("Газонная трава", "Элитная трава для газона", 500.0, 20, "Россия", "7 дней", "Зеленый")


@pytest.fixture
def lawngrass_product2():
    return LawnGrass("Газонная трава 2", "Выносливая трава", 450.0, 15, "США", "5 дней", "Темно-зеленый")
